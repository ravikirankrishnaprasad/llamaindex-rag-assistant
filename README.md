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


