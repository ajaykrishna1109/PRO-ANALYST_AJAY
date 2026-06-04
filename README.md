# 🤖 Upwork AI Copilot

Retrieval-Augmented Generation (RAG) Based Technical Documentation Assistant

## 👨‍💻 Author

**Ajay Krishna M**

Associate AI Developer Candidate
Live Demo:
https://pro-analystajay-u6sohjt6dup3xfbdgsgzgc.streamlit.app/

---

## 📌 Project Overview

Upwork AI Copilot is a Retrieval-Augmented Generation (RAG) application designed to answer questions from Upwork API documentation.

The system combines:

* Semantic Search
* Vector Databases
* Large Language Models (LLMs)
* Streamlit UI

to provide accurate, context-aware, and source-grounded responses.

The chatbot retrieves relevant documentation chunks and uses a Large Language Model to generate answers while minimizing hallucinations.

---

## 🚀 Features

* PDF Document Ingestion
* Semantic Search using Embeddings
* ChromaDB Vector Database
* Retrieval-Augmented Generation (RAG)
* DeepInfra Llama 3.1 Integration
* Streamlit Web Interface
* Source Chunk Display
* Hallucination Prevention
* Response Analytics

---

## 🏗️ Architecture

User Query
↓
Streamlit UI
↓
Retriever
↓
ChromaDB
↓
Top Relevant Chunks
↓
Llama 3.1
↓
Generated Answer
↓
Sources + Analytics

---

## 🛠️ Technology Stack

| Component        | Technology       |
| ---------------- | ---------------- |
| Language         | Python           |
| Frontend         | Streamlit        |
| Framework        | LangChain        |
| Vector Database  | ChromaDB         |
| Embeddings       | all-MiniLM-L6-v2 |
| LLM              | Meta Llama 3.1   |
| Hosting Provider | DeepInfra        |
| PDF Processing   | PyPDF            |

---

## 📂 Project Structure

```bash
upwork-ai-copilot/

├── app.py
├── ingest.py
├── rag.py
├── api.py
├── requirements.txt
├── .env
├── .env.example
├── README.md
├── chroma_db/
└── API Documentation Partial.pdf
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/upwork-ai-copilot.git
cd upwork-ai-copilot
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
DEEPINFRA_API_KEY=YOUR_API_KEY
```

Example `.env.example`

```env
DEEPINFRA_API_KEY=
```

---

## 📚 Build Vector Database

Run:

```bash
python ingest.py
```

Expected Output:

```text
Character Count: xxxx
Chunks Created: xxx
ChromaDB created successfully
```

---

## ▶️ Run Application

```bash
python -m streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## 🧠 Retrieval Pipeline

### Document Loading

* PDF loaded using PyPDF

### Text Chunking

Configuration:

```python
chunk_size = 500
chunk_overlap = 50
```

Benefits:

* Better retrieval accuracy
* Preserves context
* Reduces token waste

### Embedding Model

```text
sentence-transformers/all-MiniLM-L6-v2
```

### Vector Storage

```text
ChromaDB
```

### Retrieval

Top 8 most relevant chunks are retrieved before answer generation.

---

## 🛡️ Hallucination Prevention

Prompt Rule:

```text
Answer ONLY using the provided context.

If the answer is unavailable, respond:

"I'm sorry, but the provided documentation does not contain that information."
```

This prevents unsupported responses.

---

## 🧪 Sample Test Cases

### Query

```text
How long is an OAuth access token valid?
```

### Response

```text
24 hours
```

---

### Query

```text
How long is a refresh token valid?
```

### Response

```text
2 weeks since its last usage
```

---

### Query

```text
What OAuth scopes are available?
```

### Response

Returns the available scopes from the Upwork API documentation.

---

### Hallucination Test

```text
What is Elon Musk's phone number?
```

### Response

```text
I'm sorry, but the provided documentation does not contain that information.
```

---

## 📈 Future Enhancements

* Hybrid Search
* Cross-Encoder Re-ranking
* Multi-PDF Support
* User Authentication
* Cloud Deployment
* Conversation Memory
* Feedback Collection

---

## 📖 References

* Upwork API Documentation
* LangChain Documentation
* ChromaDB Documentation
* DeepInfra Documentation
* Streamlit Documentation
* Sentence Transformers Documentation

---

## ✅ Conclusion

This project demonstrates a complete Retrieval-Augmented Generation (RAG) workflow using ChromaDB, semantic embeddings, and Llama 3.1. The application successfully retrieves relevant documentation and generates grounded responses while reducing hallucinations through retrieval-based reasoning.
