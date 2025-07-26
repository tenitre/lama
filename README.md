# 🧠 Codebase Task Runner via Local LLM (Ollama)

A Python CLI tool that lets you analyze and process large codebases using a local LLM (via Ollama). It splits code into token-safe chunks, sends them to the LLM, and combines the responses into structured outputs like documentation or unit tests.

---

## 🚀 Features

- 🔍 Scan a codebase and break files into token-safe chunks
- 🧠 Communicate with local LLMs via Ollama
- 📄 Generate documentation, 🧪 unit tests, and ✅ TODO reports
- 🧮 Automatically calculate token usage and avoid overflows
- 📦 Supports `.py`, `.cs`, `.md`, `.ipynb`, `.json`, `.yaml`, `.toml`, and `.cfg`
- 🛠️ Extensible task engine and CLI interface
- 📚 V2: Optional RAG-based codebase indexing using embeddings

---

## 📦 Installation

```bash
# Clone this repository
git clone https://github.com/your-username/codebase-runner.git
cd codebase-runner

# Install dependencies
poetry install
```

---

## 🧑‍💻 Usage

```bash
# Basic usage
python main.py --path ./myproject --ask "Generate documentation"

# Use a specific local LLM
python main.py --path ./myproject --ask "Write unit tests" --model qwen2.5-coder
```

---

## ⚙️ Configuration

Define your available LLM models in `config/models.json`:

```json
{
  "default_model": "qwen2.5-coder",
  "models": {
    "qwen2.5-coder": {
      "url": "http://localhost:11434",
      "token_limit": 32000
    }
  }
}
```

---

## 📁 Output

- `outputs/docs/` → Markdown documentation
- `outputs/tests/` → C# unit tests
- `outputs/todos/` → TODO reports

---

## 🛣️ Roadmap

- [x] Per-file chunking and LLM interaction
- [x] Markdown and test file generation
- [x] Token-aware processing
- [ ] RAG-style indexing (V2)
- [ ] Web UI (V3)

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss your proposal.

---

## 📄 License

MIT License

---

## 🙌 Acknowledgments

- [Ollama](https://ollama.com) for local LLM orchestration
- [tiktoken](https://github.com/openai/tiktoken) for token counting
- [Nomic Embed](https://github.com/nomic-ai/nomic-embed) for vector embeddings (planned)