"""Placeholder tests for the Codebase Task Runner.

These tests currently verify that configuration loading works as
expected. Additional tests will be added as more functionality is
implemented in subsequent tasks.
"""

from pathlib import Path

import pytest

from app.config_loader import load_config, get_model_config


def test_load_config(tmp_path):
    """Ensure that the configuration loader reads and parses JSON correctly."""
    # Create a temporary configuration file
    config_data = {
        "default_model": "test-model",
        "models": {
            "test-model": {
                "url": "http://localhost:1234",
                "token_limit": 10000
            }
        }
    }
    config_path = tmp_path / "models.json"
    config_path.write_text(
        "\n".join([
            "{",
            "  \"default_model\": \"test-model\",",
            "  \"models\": {",
            "    \"test-model\": {",
            "      \"url\": \"http://localhost:1234\",",
            "      \"token_limit\": 10000",
            "    }",
            "  }",
            "}"
        ]),
        encoding="utf-8",
    )
    config = load_config(config_path)
    assert config["default_model"] == "test-model"
    assert "test-model" in config["models"]


def test_get_model_config():
    """Ensure that retrieving a model by name returns the correct config."""
    config = {
        "default_model": "a",
        "models": {
            "a": {"url": "http://example.com", "token_limit": 1234},
            "b": {"url": "http://example.org", "token_limit": 4321},
        },
    }
    model_a = get_model_config(config, "a")
    assert model_a["url"] == "http://example.com"
    assert model_a["token_limit"] == 1234

    model_b = get_model_config(config, "b")
    assert model_b["url"] == "http://example.org"
    assert model_b["token_limit"] == 4321

    with pytest.raises(KeyError):
        get_model_config(config, "nonexistent")