# 🤖 AI Teacher – Local AI Topic Explainer

AI Teacher is a **local, offline AI-powered topic explainer** built using **Streamlit** and **Ollama**.  
It uses a lightweight **Phi language model** to generate fast, clear explanations **without cloud APIs, API keys, or internet access after setup**.

This project is designed for **students, internships, academic mini-projects, demonstrations, and portfolios**.

---

## 🌟 Why AI Teacher?

Most AI tools rely on cloud services, paid APIs, and internet connectivity.  
AI Teacher proves that **powerful AI explanations can run completely on your local machine**, securely and efficiently.

---

## ✨ Key Highlights

- 🧠 Fully **local LLM** (privacy-friendly)
- ⚡ Fast responses on **CPU-only systems**
- 🔒 No API keys, tokens, or secrets
- 🌐 Works **offline after initial setup**
- 🧑‍🎓 Ideal for learning and teaching
- 💻 Clean and simple Streamlit UI
- 🛠️ Easy to extend and customize

---

## 🚀 Features

- Local AI inference using Ollama
- Lightweight Phi language model
- Question–answer based topic explanation
- Simple and intuitive interface
- Secure, offline-first design
- Low system requirements

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Language Model:** Phi  
- **Inference Engine:** Ollama (Local HTTP API)

---

## 📁 Project Structure

```text
ai-assistant/
│
├── app.py
├── backend/
│   ├── __init__.py
│   └── llm_api.py
│
├── frontend/
├── requirements.txt
├── .gitignore
└── README.md
```

# ⚙️ Installation & Setup Guide  
## AI Teacher – Local AI Topic Explainer

This document explains how to install, configure, and run **AI Teacher** on your local system using **Streamlit** and **Ollama**.

---

## ✅ Prerequisites

Ensure the following are available on your system:

- Python **3.9 or higher**
- Internet connection (required only for initial setup)
- Minimum **4 GB RAM** recommended
- Supported OS: **Windows / macOS / Linux**

---

## 1️⃣ Install Ollama

Ollama is required to run the language model locally.

### 🔹 Download Ollama
Download Ollama from the official website:

https://ollama.com/download


### 🔹 Verify Installation
Open a terminal or command prompt and run:

```bash
ollama --version

