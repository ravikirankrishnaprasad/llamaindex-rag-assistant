# 📚 LlamaIndex RAG Assistant

An **LLM-powered conversational assistant** built using **Retrieval Augmented Generation (RAG)** with **LlamaIndex**, **OpenAI**, and **Chainlit**.

This app allows users to dynamically index Wikipedia pages via prompts like `please index: <topic>` and engage in intelligent Q&A over those indexed topics.

---

## 🚀 Features

- 🔍 **Dynamic Wikipedia Indexing**  
  Ask: `please index: 2023 United States banking crisis` to index any Wikipedia page on the fly.

- 🧠 **RAG-Driven QA with LlamaIndex**  
  Combines OpenAI LLMs with LlamaIndex to answer grounded questions.

- 💬 **Conversational Chat UI with Chainlit**  
  Includes model selector and user-driven indexing via the chat interface.

- 🔐 **API Key via YAML Config**  
  Securely manages secrets using `apikeys.yaml`.

---

## 🛠️ Tech Stack

| Layer         | Technology             |
|---------------|------------------------|
| 💬 Chat UI     | [Chainlit](https://docs.chainlit.io/) |
| 🔍 RAG Engine  | [LlamaIndex](https://www.llamaindex.ai/) |
| 🤖 LLM         | [OpenAI GPT](https://platform.openai.com/) |
| 🐍 Language    | Python 3.10+            |

---

## 📁 Project Structure

```
llamaindex-rag-assistant/
├── app/                        # Python source code
│   ├── chat_agent.py           # Chainlit app entrypoint
│   ├── index_wikipages.py      # Wikipedia page loader
│   └── utils.py                # Helper for config/secrets
│
├── config/
│   └── apikeys.yaml            # API keys and secrets
│
├── docs/
│   ├── chainlit.md             # Default onboarding instructions
│   └── chainlit.en-GB.md       # Optional locale fallback
│
├── .gitignore
├── chainlit.config.toml        # Chainlit config (markdown path)
├── requirements.txt
└── README.md
```

---

## Flowchart

<img width="1755" height="1604" alt="mermaid-diagram-2025-08-24-205606" src="https://github.com/user-attachments/assets/2687d1b6-1b28-4099-84cd-77e206c1fbc2" />

---

## ⚙️ Installation

1. **Clone the Repository**
```bash
git clone https://github.com/ravikirankrishnaprasad/llamaindex-rag-assistant.git
cd llamaindex-rag-assistant
```

2. **Create a Virtual Environment**
```bash
python3 -m venv .venv
source .venv/bin/activate       # macOS/Linux
.venv\Scripts\activate        # Windows
```

3. **Install Dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Set Up API Key**
Edit `config/apikeys.yaml`:
```yaml
openai:
  api_key: sk-...
```

---

## ▶️ Running the App

Launch the Chainlit assistant:
```bash
chainlit run app/chat_agent.py -w
```

Then visit: [http://localhost:8000](http://localhost:8000)

---

## 🧪 How to Use

- 🗣 Prompt:
  ```
  please index: 2023 United States banking crisis
  ```

- 🤖 Then ask:
  ```
  What caused the 2023 US banking crisis?
  ```

The assistant indexes the page in real-time and responds with grounded, factual insights from Wikipedia.

---
## Test cases:
<img width="834" height="656" alt="Screenshot 2025-08-24 at 4 06 30 PM" src="https://github.com/user-attachments/assets/c40f815d-365c-45d1-a0ac-0228afbb66c9" />

---
## ReAct logs:
<img width="1164" height="467" alt="Screenshot 2025-08-24 at 4 05 55 PM" src="https://github.com/user-attachments/assets/d4b1ad08-a128-4277-951d-969d7d95c8c3" />



## 🎯 Learning Objectives

- How to integrate **retrieval with LLMs** using LlamaIndex.
- Building **dynamic conversational agents** with Chainlit.
- Managing **external data sources** in a RAG pipeline.
- Structuring clean Python applications for GenAI workflows.

---

## 🚧 Future Improvements

- Add PDF / CSV / Doc ingestion
- Integrate vector databases (FAISS, Pinecone, Weaviate)
- Support long-term chat memory and citations
- Deploy via Docker, Streamlit, or Hugging Face Spaces

---

## 📜 License

Licensed under the [Apache License 2.0](./LICENSE)

---

## 👨‍💻 Author

**Ravikiran Krishnaprasad**  
Development Architect | AI/ML & GenAI Innovator  
[GitHub Portfolio](https://github.com/ravikirankrishnaprasad/portfolio) | [LinkedIn](https://linkedin.com/in/ravikirankrishnaprasad)
