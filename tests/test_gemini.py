import os
import pytest
from unittest import mock
from dotenv import load_dotenv
from src.gemini import _prompt


@pytest.fixture
def set_gemini_env():
    # Load .env file, overriding existing environment variables
    load_dotenv(override=True)


def test_prompt(set_gemini_env):
    """Tests that the prompt function returns a string."""
    test_prompt_text = "What today's date?"
    response = _prompt(test_prompt_text)

    assert isinstance(response, str)
