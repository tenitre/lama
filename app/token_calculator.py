"""Utilities for counting tokens using the tiktoken library."""

from __future__ import annotations

from typing import Optional
import logging

try:
    import tiktoken
except Exception:  # pragma: no cover - tiktoken may not be installed
    tiktoken = None  # type: ignore

__all__ = ["count_tokens"]

logger = logging.getLogger(__name__)


def _get_encoding(model: Optional[str] = None):
    """Return a tiktoken encoding for ``model`` if available."""
    if tiktoken is None:
        return None
    try:
        if model:
            return tiktoken.encoding_for_model(model)
        return tiktoken.get_encoding("gpt2")
    except Exception as exc:  # pragma: no cover - network failures etc.
        logger.debug("tiktoken failed: %s", exc)
        return None


def count_tokens(text: str, model: Optional[str] = None) -> int:
    """Return the number of tokens in ``text`` for the given model."""
    encoding = _get_encoding(model)
    if encoding is None:
        # fallback simple approximation when tiktoken is unavailable
        return len(text.split())
    try:
        return len(encoding.encode(text))
    except Exception as exc:  # pragma: no cover - network failures etc.
        logger.debug("tiktoken encode failed: %s", exc)
        return len(text.split())
