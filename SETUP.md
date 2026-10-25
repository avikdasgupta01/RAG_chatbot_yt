# Setup Instructions for the RAG Chatbot Project

This project uses `uv` to manage Python dependencies and the virtual environment.

## 1) Install `uv`

Open a terminal in the project root and run:

```bash
pip install uv
```

## 2) Install project dependencies

From the project root:

```bash
uv sync
```

This creates the virtual environment and installs the dependencies listed in `pyproject.toml`.

## 3) Activate the virtual environment

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

## 4) Select the correct Python interpreter in VS Code

In VS Code:

1. Open the Command Palette: `Ctrl+Shift+P`
2. Run: `Python: Select Interpreter`
3. Choose the interpreter from the `.venv` folder created by `uv`
4. If using Jupyter notebooks, also select that same environment for the notebook kernel

You should see something like:

- `.venv/bin/python` on macOS/Linux
- `.venv\Scripts\python.exe` on Windows

## 5) Use Jupyter with the same environment

If the notebook does not automatically detect the environment:

1. Open the notebook
2. In the top-right kernel selector, choose the `uv` environment / `.venv`
3. If needed, use `Python: Select Interpreter` again and pick the same environment

## 6) Run the project

You can run Python scripts from the terminal after activation:

```bash
python llm_test.py
```

or for notebook-based work, open the notebook and make sure the selected kernel is the same `.venv` interpreter.

## Troubleshooting

If `uv` is not recognized:

```bash
python -m pip install --upgrade pip
pip install uv
```

If dependencies are missing, run:

```bash
uv sync
```

If the notebook kernel still does not show the environment, restart VS Code and re-select the interpreter.
