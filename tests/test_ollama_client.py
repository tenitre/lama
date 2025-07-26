"""Tests for the Ollama API client."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.ollama_client import OllamaClient


def test_ollama_client_chat(monkeypatch):
    calls = {}

    class FakeResp:
        status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            return {"choices": [{"message": {"content": "hello"}}]}

    def fake_post(url, json, timeout=60):
        calls["url"] = url
        calls["json"] = json
        return FakeResp()

    import requests

    monkeypatch.setattr(requests, "post", fake_post)

    client = OllamaClient("http://localhost:11434")
    result = client.chat("model", [{"role": "user", "content": "hi"}])
    assert result == "hello"
    assert calls["json"]["model"] == "model"

