"""Core application package for the Codebase Task Runner.

This package will contain modules responsible for scanning files,
chunking content, communicating with a local LLM via Ollama, and
writing results. For now only configuration helpers are defined here.
"""

__all__ = [
    "config_loader",
]