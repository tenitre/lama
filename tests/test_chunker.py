"""Tests for the chunking utilities."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.chunker import chunk_file
from app.token_calculator import count_tokens


def test_chunk_file_splits(tmp_path):
    # create a file with repeating lines
    content = "\n".join([f"line {i}" for i in range(50)])
    path = tmp_path / "big.py"
    path.write_text(content, encoding="utf-8")

    chunks = chunk_file(path, max_tokens=10)
    assert chunks, "Expected at least one chunk"
    # ensure combined content equals original content
    combined = "\n".join(chunk.content for chunk in chunks)
    assert combined == content
    # each chunk should not exceed the token limit
    for chunk in chunks:
        assert len(chunk.content.splitlines()) > 0
        assert len(chunk.content) > 0
        # verify token count respects the limit
        assert count_tokens(chunk.content) <= 10
