# Gemini MCP Server

This project provides a `fastmcp` server that interacts with the Google Gemini AI model using the `openai` library. It allows you to generate text from the Gemini model by sending prompts to the server.

## Features

- **Gemini AI Integration**: Utilizes the `google-genai` library to communicate with the Google Gemini AI model, including support for Google Search grounding.
- **`fastmcp` Server**: Exposes a `prompt` tool via a `fastmcp` server for easy integration with `fastmcp` clients.
- **Environment Variable Configuration**: API key and model name are configured via environment variables (`GEMINI_API_KEY`, `GEMINI_MODEL`).
- **Testable**: Includes `pytest` for unit testing with mocked API calls.

## Installation

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone https://github.com/cdecl/gemini-mcp.git
    cd gemini-mcp
    ```

2.  **Install `uv` (if you don't have it):**
    `uv` is a fast Python package installer and resolver.
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    Make sure `uv` is in your PATH.

3.  **Install dependencies:**
    This project uses `pyproject.toml` for dependency management.
    ```bash
    uv pip install -e .
    ```



## Running the MCP Server

You can run the `fastmcp` server using the registered script entry point:

```bash
uvx gemini-mcp
```

Alternatively, you can run it directly:

```bash
python src/gemini_mcp/gemini.py
```

This will start the `fastmcp` server, listening for incoming requests.

## Using with `mcp.json` Configuration

For `fastmcp` clients, you can use the provided `mcp.json` file to configure the server connection.

**`mcp.json` example:**

```json
{
  "mcpServers": {
    "gemini": {
      "command": "uv",
      "args": [
        "run", 
        "--directory",
        "path_to_/gemini-mcp/",
        "path_to_/gemini-mcp/src/gemini_mcp/gemini.py"
      ],
      "env": {
        "GEMINI_API_KEY": "YOUR_API_KEY_HERE",
        "GEMINI_MODEL": "gemini-2.5-flash"
      }
    }
  }
}
```

**Note**: Remember to replace `YOUR_API_KEY_HERE` with your actual Gemini API key in `mcp.json` if you use this method. The `args` path should also be adjusted if your project is located elsewhere. The `env` section in `mcp.json` allows you to set environment variables specifically for the `fastmcp` server process.

With this `mcp.json` configured, a `fastmcp` client can discover and interact with your Gemini server.

## Running Tests

To run the unit tests, use `pytest`:

```bash
.venv/bin/pytest
```

**Note**: The tests mock the actual API calls, so you don't need a valid API key to run them. However, the `GEMINI_API_KEY` environment variable must be set (even to a dummy value like `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`) for the `openai` client initialization to pass client-side validation.
