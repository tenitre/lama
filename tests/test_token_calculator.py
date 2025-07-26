"""Tests for the token calculator utilities."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.token_calculator import count_tokens


def test_count_tokens_basic():
    text = "hello world"
    tokens = count_tokens(text)
    assert isinstance(tokens, int)
    assert tokens > 0
