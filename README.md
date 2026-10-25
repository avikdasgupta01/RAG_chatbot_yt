# RAG Chatbot YT

A lightweight Retrieval-Augmented Generation (RAG) project for experimenting with local document search and LLM-powered Q&A. The project ingests a PDF document, stores vector embeddings in a local Qdrant database, and answers questions by combining semantic retrieval with Groq/OpenAI-compatible models.

## Overview

This repository is designed as a practical starter for:

- loading a PDF-based knowledge base
- chunking and embedding document content
- storing vectors in Qdrant
- retrieving the most relevant context for a user question
- generating an answer using an LLM via Groq or OpenAI endpoints

It includes a sample employee handbook PDF and a notebook for a traditional RAG workflow.

## Project Structure

```text
.
├── README.md
├── SETUP.md
├── pyproject.toml
├── uv.lock
├── .env_example
├── documents/
│   └── sample_employee_handbook.pdf
├── qdrant_storage/
│   ├── meta.json
│   └── collection/
│       └── simple_rag/
│           └── storage.sqlite
└── src/
    └── rag_chatbot_yt/
        ├── Groq_client_llm_test.py
        ├── Openai_client_llm_test.py
        ├── Traditional RAG Sample.ipynb
        └── __init__.py
```

## Tech Stack

- Python 3.12+
- uv for dependency management
- Qdrant for vector storage
- sentence-transformers for embeddings
- Groq and OpenAI Python clients
- PyMuPDF for PDF parsing
- python-dotenv for environment management

## Prerequisites

Before running the project, make sure you have:

- Python 3.12 or newer
- uv installed
- access to a Groq or OpenAI API key

## Setup

1. Install uv:

```bash
pip install uv
```

2. Install project dependencies:

```bash
uv sync
```

3. Copy the environment template and add your API keys:

```bash
cp .env_example .env
```

Then update `.env` with your credentials:

```env
GROQ_API_KEY=your_groq_key
OPENAI_API_KEY=your_openai_key
HF_TOKEN=
```

4. Activate the virtual environment:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

## Running the Project

### LLM checks

You can test the model clients directly:

```bash
python src/rag_chatbot_yt/Groq_client_llm_test.py
python src/rag_chatbot_yt/Openai_client_llm_test.py
```

### Notebook workflow

Open the notebook:

- `src/rag_chatbot_yt/Traditional RAG Sample.ipynb`

This notebook demonstrates the traditional RAG flow:

1. load a PDF
2. split text into chunks
3. generate embeddings
4. store them in Qdrant
5. query the vector store
6. pass retrieved context to an LLM

## Notes

- The PDF in `documents/` is a sample document for experimentation.
- Qdrant storage is kept in the local `qdrant_storage/` directory.
- For detailed environment configuration, see `SETUP.md`.

## License

This project does not currently declare a license. Add one if you plan to share or distribute it publicly.
