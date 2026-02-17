# 🧠 DocuMind-
> **Local Agentic RAG System with FastAPI & Streamlit**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 Overview
**RAG-Agent-** is a sophisticated Retrieval-Augmented Generation (RAG) system that runs entirely locally. Unlike standard RAG pipelines, this project implements an **Agentic approach**: the AI "brain" (Llama 3) autonomously decides *when* to search your documents and *how* to synthesize the answer.

It features a high-performance **FastAPI backend** for processing and a beautiful, dark-mode **Streamlit frontend** for interaction.

---

## ✨ Features
* **🤖 Agentic Reasoning:** Uses LangChain's ReAct agent to "think" before answering.
* **🔒 100% Local:** Runs on your machine using **Ollama** (Llama 3) and **ChromaDB**. No data leaves your computer.
* **⚡ High Performance:** Backend built with FastAPI for asynchronous request handling.
* **🎨 Aesthetic UI:** A custom-styled Streamlit interface with glassmorphism effects and dark mode.
* **📄 PDF Ingestion:** Automatically chunks, embeds, and stores PDF content for retrieval.

---

## 🛠️ Tech Stack
* **LLM Engine:** [Ollama](https://ollama.com/) (Llama 3)
* **Orchestration:** LangChain
* **Vector Database:** ChromaDB
* **Backend API:** FastAPI & Uvicorn
* **Frontend:** Streamlit
* **Embeddings:** Nomic-Embed-Text

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.10+** and **[Ollama](https://ollama.com/)** installed.

Pull the required models:
```bash
ollama pull llama3
ollama pull nomic-embed-text

