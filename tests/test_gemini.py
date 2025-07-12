import os
import pytest
from src.gemini import _prompt


@pytest.fixture
def set_gemini_env():
    os.environ["GEMINI_API_KEY"] = "test_key"
    os.environ["GEMINI_MODEL"] = "test_model"
    yield
    del os.environ["GEMINI_API_KEY"]
    del os.environ["GEMINI_MODEL"]


def test_prompt():
    """Tests that the prompt function returns a string."""
    test_prompt_text = "Hello, test!"
    response = _prompt(test_prompt_text)
    assert isinstance(response, str)
    # assert test_prompt_text in response