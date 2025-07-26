"""Utilities for splitting files into token-limited chunks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional
import logging

from .token_calculator import count_tokens

__all__ = ["Chunk", "chunk_file"]

logger = logging.getLogger(__name__)


@dataclass
class Chunk:
    """Representation of a chunk of a source file."""

    file: Path
    index: int
    start_line: int
    end_line: int
    content: str


def chunk_file(path: Path, max_tokens: int, model: Optional[str] = None) -> List[Chunk]:
    """Split a file into ``Chunk`` objects obeying ``max_tokens``."""
    if not path.is_file():
        raise FileNotFoundError(path)

    lines = path.read_text(encoding="utf-8").splitlines()
    chunks: List[Chunk] = []

    start = 0
    current_lines: List[str] = []
    for idx, line in enumerate(lines, start=1):
        current_lines.append(line)
        tokens = count_tokens("\n".join(current_lines), model)
        if tokens > max_tokens and current_lines:
            # remove last line and flush
            current_lines.pop()
            chunk_text = "\n".join(current_lines)
            if chunk_text:
                chunk = Chunk(
                    file=path,
                    index=len(chunks),
                    start_line=start + 1,
                    end_line=idx - 1,
                    content=chunk_text,
                )
                logger.debug("Created chunk %s lines %s-%s", chunk.index, chunk.start_line, chunk.end_line)
                chunks.append(chunk)
            # start new chunk with current line
            current_lines = [line]
            start = idx - 1
    # flush remaining
    if current_lines:
        chunk = Chunk(
            file=path,
            index=len(chunks),
            start_line=start + 1,
            end_line=len(lines),
            content="\n".join(current_lines),
        )
        logger.debug("Created chunk %s lines %s-%s", chunk.index, chunk.start_line, chunk.end_line)
        chunks.append(chunk)
    return chunks
