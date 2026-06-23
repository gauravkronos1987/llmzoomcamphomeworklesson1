# llmzoomcamphomeworklesson1

A homework project for the DataTalksClub LLM Zoomcamp lesson, demonstrating a simple retrieval-augmented generation (RAG) workflow using OpenAI, minsearch, and GitHub source data.

## Project overview

This repository contains:

- `homeworklesson1.ipynb` - Jupyter notebook for exploring OpenAI Responses, gitsource data ingestion, search indexing, and RAG-style QA.
- `main.py` - minimal Python entry point that prints a startup message.
- `rag_helper.py` - reusable `RAGBase` helper class for search, prompt construction, and LLM calls.
- `rag_helper_lesson1_hw.py` - lesson-specific subclass extending `RAGBase` for custom lesson search behavior.
- `pyproject.toml` - project metadata and dependency list.

## Dependencies

This project is built for Python 3.12+ and depends on:

- `openai`
- `gitsource`
- `jupyter`
- `langchain`
- `langchain-community`
- `langchain-openai`
- `langgraph`
- `minsearch`
- `python-dotenv`
- `requests`

### Install with `uv`

If you are using the same environment setup as the notebook, install the dependencies with:

```bash
uv add gitsource jupyter langchain langchain-community langchain-openai langgraph minsearch openai python-dotenv requests
```

### Install with `pip`

If you prefer pip, install the same dependencies manually:

```bash
python -m pip install openai gitsource jupyter langchain langchain-community langchain-openai langgraph minsearch python-dotenv requests
```

## Configuration

Create a `.env` file at the repository root with your OpenAI API key:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

The notebook and helper code use `python-dotenv` to load this environment variable.

## Usage

### Run the notebook

Open the notebook in Jupyter and run the cells in order:

```bash
jupyter notebook homeworklesson1.ipynb
```

The notebook performs these main steps:

1. Loads the OpenAI client.
2. Downloads lesson content from GitHub using `gitsource`.
3. Builds a search index with `minsearch`.
4. Uses a `RAGWithLessonSearch` assistant to query indexed lesson content.

### Run the main script

The repository includes a simple entry point for verification:

```bash
python main.py
```

## How the RAG helper works

- `rag_helper.py` defines `RAGBase`.
- `RAGBase` performs a search, constructs a prompt, and calls the OpenAI `responses.create` API.
- `rag_helper_lesson1_hw.py` extends `RAGBase` to customize search behavior and context formatting for this lesson.

## Notes

- The notebook downloads and indexes lesson documents from the DataTalksClub `llm-zoomcamp` repository.
- This project is intended for experimentation and learning rather than production use.
- Make sure your OpenAI key is valid and has access to the `responses` API.

## File structure

- `homeworklesson1.ipynb` - main notebook for the lesson.
- `main.py` - simple Python script.
- `rag_helper.py` - base RAG helper class.
- `rag_helper_lesson1_hw.py` - lesson-specific assistant subclass.
- `pyproject.toml` - package metadata and dependencies.

## License

This repository does not include a license file. Add one if you want to share or reuse the code publicly.