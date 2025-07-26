"""Tests for the task dispatcher logic."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.task_dispatcher import TaskDispatcher
from app.ollama_client import OllamaClient
from app.chunker import Chunk


def test_dispatcher_combines_chunks(monkeypatch, tmp_path):
    file_path = tmp_path / "f.py"
    file_path.write_text("dummy", encoding="utf-8")

    chunks = [
        Chunk(file=file_path, index=0, start_line=1, end_line=1, content="a"),
        Chunk(file=file_path, index=1, start_line=2, end_line=2, content="b"),
    ]

    def fake_chunk_file(path, max_tokens, model=None):
        return chunks

    monkeypatch.setattr("app.task_dispatcher.chunk_file", fake_chunk_file)

    calls = []

    def fake_chat(self, model, messages):
        calls.append(messages[0]["content"])
        if len(calls) < 3:
            return f"resp{len(calls)}"
        return "combined"

    monkeypatch.setattr(OllamaClient, "chat", fake_chat)

    client = OllamaClient("http://localhost:11434")
    dispatcher = TaskDispatcher(client, "model", token_limit=10)
    result = dispatcher.run_task_on_file(file_path, "Summarize")

    assert result == "combined"
    assert len(calls) == 3

