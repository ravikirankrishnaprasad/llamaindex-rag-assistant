# 📚 LlamaIndex RAG Assistant

An **LLM-powered conversational assistant** built with **Retrieval Augmented Generation (RAG)** using **LlamaIndex, OpenAI, and Chainlit**.  
This project demonstrates how to enhance Large Language Models with external knowledge sources (Wikipedia in this case) to deliver accurate, context-aware responses.

---

## 🚀 Features
- 🔎 **RAG Integration** – Combines OpenAI LLMs with LlamaIndex for retrieval-augmented responses.  
- 📖 **Wikipedia Knowledge Access** – Augments chatbot knowledge with selected Wikipedia pages.  
- 💬 **Conversational Interface** – Built with Chainlit for an interactive chat UI.  
- 🧠 **Context-Aware Answers** – Reduces hallucinations by grounding responses in retrieved documents.  

---

## 🛠️ Tech Stack
- **[OpenAI](https://platform.openai.com/)** – Large Language Model  
- **[LlamaIndex](https://www.llamaindex.ai/)** – Retrieval-Augmented Generation framework  
- **[Chainlit](https://docs.chainlit.io/)** – Conversational UI for LLM apps  
- **Python 3.10+** – Core programming language  

---

## 📂 Project Structure
```
llamaindex-rag-assistant/
│── data/                # Wikipedia page(s) stored locally or via API
│── app.py               # Main Chainlit application
│── rag_engine.py        # RAG pipeline with LlamaIndex
│── requirements.txt     # Python dependencies
│── LICENSE              # License file (Apache 2.0)
│── README.md            # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**  
```bash
git clone https://github.com/<your-username>/llamaindex-rag-assistant.git
cd llamaindex-rag-assistant
```

2. **Create virtual environment & install dependencies**  
```bash
python3 -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scriptsctivate      # On Windows

pip install -r requirements.txt
```

3. **Set your OpenAI API Key**  
```bash
export OPENAI_API_KEY="your-api-key"   # Mac/Linux
setx OPENAI_API_KEY "your-api-key"     # Windows
```

---

## ▶️ Usage

Run the chatbot with:
```bash
chainlit run app.py
```

Then open [http://localhost:8000](http://localhost:8000) in your browser to start chatting with the assistant.

---

## 📖 Example Use Case
**Query:**  
```
Tell me about the life of Nikola Tesla.
```

**Response:**  
> The assistant retrieves facts from the selected Wikipedia page on **Nikola Tesla**, and the LLM generates a conversational, accurate response grounded in that content.

---

## 🎯 Learning Objectives
- Understand how to build **RAG pipelines** with LlamaIndex.  
- Explore conversational interfaces with **Chainlit**.  
- Learn how to **augment LLMs with external knowledge sources**.  

---

## 🏗️ Future Enhancements
- Add support for **multiple data sources** (PDFs, docs, websites, enterprise data).  
- Integrate with **vector databases** (Pinecone, Weaviate, FAISS).  
- Extend UI with **session memory & conversation history**.  
- Deploy to **cloud environments** (AWS/GCP/Azure).  

---

## 📜 License
This project is licensed under the **Apache License 2.0** - see the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 Author
**Ravikiran**  
Development Architect | AI/ML & Generative AI Enthusiast  
