"""Coordinate sending file chunks to Ollama and combining the results."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import List

from .chunker import chunk_file, Chunk
from .ollama_client import OllamaClient

__all__ = ["TaskDispatcher"]

logger = logging.getLogger(__name__)


class TaskDispatcher:
    """Send chunks for a task and combine responses per file."""

    def __init__(self, client: OllamaClient, model: str, token_limit: int) -> None:
        self.client = client
        self.model = model
        self.token_limit = token_limit

    def run_task_on_file(self, path: Path, ask: str) -> str:
        """Process ``path`` using ``ask`` and return combined LLM output."""
        chunks = chunk_file(path, max_tokens=self.token_limit)
        responses: List[str] = []
        for chunk in chunks:
            prompt = (
                f"{ask}\n\nFile: {chunk.file.name}\n"
                f"Lines {chunk.start_line}-{chunk.end_line}:\n{chunk.content}"
            )
            messages = [{"role": "user", "content": prompt}]
            logger.debug("Sending chunk %s of %s", chunk.index, path)
            responses.append(self.client.chat(self.model, messages))

        combine_lines = [
            "Combine the following chunk results into a single answer:",
        ]
        for idx, resp in enumerate(responses):
            combine_lines.append(f"Chunk {idx}: {resp}")
        final_prompt = "\n".join(combine_lines)
        final_msg = [{"role": "user", "content": final_prompt}]
        return self.client.chat(self.model, final_msg)

