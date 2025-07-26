# 📄 Project Documentation: Codebase Task Runner via Local LLM (Ollama)

## 📌 Product Requirements Document (PRD)

# Product Requirements Document (PRD): Codebase Task Runner via Local LLM (Ollama)

## 🎯 Objective
Create a Python CLI tool (managed via Poetry) that enables developers to process large codebases using a local LLM via Ollama. The tool sends code in token-safe chunks, executes user-defined tasks (e.g., documentation, unit tests, TODOs), and assembles the results intelligently.

## 👤 Target Users
- Developers using local LLMs (e.g., Qwen, LLaMA) via Ollama.
- Secure environments that cannot use cloud-based LLMs.
- Engineers wanting full automation and insight across codebases.

## 🔍 Core Features

### 1. Folder Scanner
- Accepts a directory path via CLI.
- Recursively finds supported files:
  - `.py`, `.cs`, `.md`, `.ipynb`, `.json`, `.yaml`, `.toml`, `.cfg`
- Respects common exclusions (e.g., `__pycache__`, `.git`, `.env`, etc).

### 2. Token Calculator
- Calculates tokens for:
  - Each file
  - Each chunk
  - Overall task request
- Uses a compatible tokenizer (e.g., tiktoken).

### 3. Chunking Engine
- Splits large files into token-safe chunks.
- Stores metadata (filename, line range, chunk index).
- Groups small files when possible.

### 4. LLM Communicator (via Ollama)
- Sends chunks sequentially to the LLM.
- Gathers intermediate results and combines them per file.
- Final prompt combines per-file answers into a single result.

### 5. Task Dispatcher
- Supports tasks like:
  - `"Generate documentation"`
  - `"Write unit tests"`
  - `"Find TODOs"`
- CLI usage:  
  ```bash
  python main.py --path ./project --ask "Generate documentation"
  ```

### 6. Result Combiner
- Combines per-file results into:
  - `.md` for documentation
  - `.cs` for unit tests
  - `.txt` for TODO findings

### 7. Output Writer
- Writes output to structured folders.
  - `outputs/docs/`, `outputs/tests/`, `outputs/todos/`
- Adds headers and timestamps.

### 8. Logging
- Uses Python’s `logging` module.
- Logs visible in terminal by default.
- Tracks:
  - Token usage
  - File and chunk processing
  - Errors and outputs

## 📉 Context Strategy
- Each run is stateless.
- Model memory is not persisted.
- Future V2: add codebase indexing using embeddings and vector search (RAG).

## ❌ Non-Goals (V1)
- Persistent memory
- Parallel chunk execution
- GUI (initially CLI-only)

## 🚀 Future Enhancements (V2+)
- Web UI (Streamlit/Gradio)
- Conversational assistant
- Vector-based codebase indexing (RAG)
- Incremental processing via file change detection

---

## 🧱 Software Design Document

# Software Design Document: Codebase Task Runner via Local LLM (Ollama)

## 1. Introduction and Overview

### Project Description
This project is a Python CLI tool, managed via Poetry, that enables developers to perform codebase-level tasks by sending large files to a local LLM (Ollama) in token-safe chunks. Tasks include generating documentation, writing unit tests, and identifying TODOs. The system handles token limits by chunking input, collecting intermediate responses, and assembling a final result.

### Objectives
- Enable safe and efficient communication with local LLMs under token constraints.
- Provide modular, multi-step task execution for large codebases.
- Support markdown, configuration, and code files for analysis.
- Deliver CLI usability with optional extensibility into web UIs.

### Document Overview
This document details the system architecture, data design, interfaces, components, assumptions, and UI structure. It serves as a blueprint for development.

---

## 2. System Architecture

### High-Level Architecture Diagram
```
User CLI Input
    ↓
Folder Scanner → Token Calculator → Chunking Engine
    ↓                             ↘
Task Dispatcher ← Ollama Client ← Chunked Input
    ↓
Combiner → Output Writer → Logs & Results
```

### Major Components
- Folder Scanner: Collects files to process.
- Token Calculator: Measures token usage.
- Chunker: Splits input files into safe sizes.
- Ollama Client: Sends/receives requests from the local LLM.
- Task Dispatcher: Manages orchestration of task flow.
- Output Writer: Persists results into `.md`, `.cs`, or `.txt`.

### Design Patterns & Trade-offs
- Stateless sessions for simplicity and predictability.
- Token-first processing model to minimize overflow errors.
- Optional summarization layer planned for future scalability.

---

## 3. Data Design

### Token Flow and Chunking
- `tiktoken`-style tokenizer for compatibility with model limits.
- Chunk metadata includes: filename, lines covered, chunk ID.
- Token counts per file and chunk are logged.

### Output Structure
- Output directory contains subfolders by task:
  - `docs/`, `tests/`, `todos/`

### Data Integrity
- Chunks validated for completeness before LLM processing.
- Combined results reviewed before output generation.

---

## 4. Interface Design

### Internal Interfaces
- Functions between modules pass structured file metadata and chunk content.

### External Interfaces
- Ollama REST API: Local LLM interface via `/v1/chat/completions`

### API Message Format (Ollama)
```json
{
  "model": "qwen:14b",
  "messages": [{"role": "user", "content": "your message here"}]
}
```

### Security and Authentication
- Localhost-only requests; no remote API exposure.
- No authentication for CLI; intended for single-user desktop.

---

## 5. Component Design

### Folder Scanner
- Recursively walks directories.
- Filters by extension.

### Token Calculator
- Uses tokenizer to count tokens per chunk/file.

### Chunking Engine
- Ensures files fit under token limits.
- Yields multiple chunks if needed.

### Ollama Client
- Sends one chunk at a time.
- Collects responses.
- Sends follow-up prompt to "combine" per-file answers.

### Combiner
- Assembles all per-file results into a global answer.

### Output Writer
- Detects output type by task.
- Writes `.cs` for unit tests, `.md` for documentation.

---

## 6. User Interface Design

### CLI
- `--path ./project --ask "Write docs"` style interface.
- Logging to console and log file.

### Future Web UI (Planned)
- Streamlit or Gradio interface.
- Drag & drop file support.
- Progress bar, logs, result viewer.

---

## 7. Assumptions and Dependencies

### Assumptions
- Ollama is running on `localhost`.
- Each model has a defined token limit (e.g., 32K).
- Code files are valid and parseable.

### Dependencies
- `Poetry`
- `requests` (or `httpx`)
- `tiktoken` or model-compatible tokenizer
- `logging` module

---

## 8. Glossary of Terms

| Term       | Definition |
|------------|------------|
| Token      | A unit of text used by LLMs. |
| Ollama     | A local LLM server for running models. |
| Chunk      | A section of code split by token limits. |
| Task       | A user-defined instruction like “write docs”. |
| CLI        | Command Line Interface. |
| `.cs` file | C# source code file. |

---

## ✅ Best Practices Applied
- Simple, clear structure.
- Logs and outputs built-in.
- Summarization layer deferred to future.
- Token-first architecture ensures LLM safety.
- CLI-focused, with modularity for future UI.

---

## ✅ Task List

## Relevant Files

- `main.py` - Entry point for the CLI interface and task orchestration.
- `config/models.json` - Defines available LLM models, their API URLs, and token limits.
- `app/folder_scanner.py` - Scans project directories and filters files.
- `app/token_calculator.py` - Calculates token size of files and chunks.
- `app/chunker.py` - Splits files into token-safe chunks.
- `app/ollama_client.py` - Sends and receives messages to/from Ollama local LLM API.
- `app/task_dispatcher.py` - Coordinates task execution across files and chunks.
- `app/output_writer.py` - Saves output to correct format and location.
- `app/indexer.py` - (V2) Builds and stores vector embeddings of files using Nomic Embed.
- `app/retriever.py` - (V2) Retrieves relevant chunks based on user query using vector similarity.
- `logs/app.log` - Captures CLI activity and status (for future extension).

### Notes

- All modules should use Python’s `logging` module for consistent, terminal-visible output.
- Unit tests should be placed in corresponding `test_*.py` files within a `tests/` folder.
- Use `pytest` to run tests. Example: `pytest tests/test_chunker.py`

## Tasks

- [x] 1.0 Setup Project Structure and Config
  - [x] 1.1 Create base project structure using Poetry
  - [x] 1.2 Create `/app`, `/config`, `/outputs`, and `/tasks` folders
  - [x] 1.3 Create `config/models.json` with LLM name, URL, and token limits
  - [x] 1.4 Load JSON config and support CLI override for model name
  - [x] 1.5 Add initial test folder with placeholder tests

- [x] 2.0 Implement File Scanning and Filtering
  - [x] 2.1 Implement recursive directory scanning
  - [x] 2.2 Filter files by allowed extensions (.py, .cs, .md, .ipynb, etc.)
  - [x] 2.3 Exclude folders like .git, __pycache__, .env, node_modules
  - [x] 2.4 Return structured list of file paths and metadata

- [ ] 3.0 Implement Token Calculation and Chunking
  - [ ] 3.1 Integrate token counting using a compatible tokenizer
  - [ ] 3.2 Implement chunk splitting with metadata (filename, line range, chunk number)
  - [ ] 3.3 Ensure token limits are respected and logged
  - [ ] 3.4 Add test cases for large and edge-case files

- [ ] 4.0 Implement Ollama Communication and Task Flow
  - [ ] 4.1 Implement API client for Ollama local server
  - [ ] 4.2 Send each chunk with user-defined prompt
  - [ ] 4.3 Gather responses per chunk
  - [ ] 4.4 Send follow-up prompt to combine per-file responses
  - [ ] 4.5 Allow prompt reuse across files

- [ ] 5.0 Implement Output Aggregation and File Writing
  - [ ] 5.1 Create markdown output writer for documentation
  - [ ] 5.2 Create .cs writer for unit test generation
  - [ ] 5.3 Organize outputs by task (docs/, tests/, todos/)
  - [ ] 5.4 Add timestamped logs or headers to outputs
  - [ ] 5.5 Validate and log file save success

- [ ] 6.0 Add CLI Interface and Logging
  - [ ] 6.1 Build CLI using argparse or click
  - [ ] 6.2 Accept --path, --ask, --model as arguments
  - [ ] 6.3 Add centralized logging to terminal using Python logging
  - [ ] 6.4 Ensure key steps (scan, chunk, send, write) are logged clearly

- [ ] 7.0 (V2) Implement Codebase Indexing and Retrieval
  - [ ] 7.1 Integrate Nomic Embed to convert file chunks to embeddings
  - [ ] 7.2 Store embeddings in a local vector store (e.g., FAISS)
  - [ ] 7.3 Implement retriever to match query to most relevant chunks
  - [ ] 7.4 Format retrieved chunks and send to Ollama for response
  - [ ] 7.5 Add fallback logic when no relevant chunks are retrieved