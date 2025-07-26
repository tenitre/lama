"""Simple API client for communicating with a local Ollama server."""

from __future__ import annotations

import logging
from typing import Dict, List

import requests

__all__ = ["OllamaClient"]

logger = logging.getLogger(__name__)


class OllamaClient:
    """HTTP client for the Ollama chat completion API."""

    def __init__(self, base_url: str, timeout: int = 300) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def chat(self, model: str, messages: List[Dict[str, str]]) -> str:
        """Send a chat completion request and return the LLM response text."""
        url = f"{self.base_url}/v1/chat/completions"
        payload = {"model": model, "messages": messages}
        logger.debug("POST %s", url)
        response = requests.post(url, json=payload, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        try:
            return data["choices"][0]["message"]["content"]
        except (KeyError, IndexError) as exc:  # pragma: no cover - invalid reply
            logger.error("Unexpected response from Ollama: %s", data)
            raise RuntimeError("Invalid response from Ollama") from exc
