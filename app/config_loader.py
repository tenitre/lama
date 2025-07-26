"""Helper functions for loading and querying model configuration.

This module reads a JSON configuration file containing model
definitions and exposes utility functions to load that data and
retrieve a specific model's configuration. The configuration file
follows the structure documented in the project PRD.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any


def load_config(path: Path) -> Dict[str, Any]:
    """Load the model configuration from a JSON file.

    Parameters
    ----------
    path : Path
        Path to the JSON configuration file.

    Returns
    -------
    dict
        The parsed configuration dictionary.

    Raises
    ------
    ValueError
        If the file cannot be parsed as valid JSON.
    FileNotFoundError
        If the file does not exist.
    """
    with path.open("r", encoding="utf-8") as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON in configuration file: {exc}") from exc
    return config


def get_model_config(config: Dict[str, Any], name: str) -> Dict[str, Any]:
    """Retrieve a model configuration by name from the loaded config.

    Parameters
    ----------
    config : dict
        The loaded configuration dictionary containing 'models' and
        'default_model' keys.
    name : str
        The name of the model to retrieve. If this model is not found
        a KeyError is raised.

    Returns
    -------
    dict
        The configuration dictionary for the requested model.

    Raises
    ------
    KeyError
        If the specified model name is not present in the config.
    """
    models = config.get("models", {})
    if name not in models:
        raise KeyError(f"Model '{name}' not found in configuration")
    return models[name]