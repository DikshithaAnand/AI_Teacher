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

# ⚙️ Installation & Setup  
## AI Teacher – Local AI Topic Explainer

This section provides the complete installation and setup steps in a **clean, neat Markdown format**, starting from download to running the application.

---

## 1️⃣ Download Ollama

Ollama is required to run the language model locally.

- Visit the official website:  
  https://ollama.com/download
- Download the installer for your operating system (**Windows / macOS / Linux**)
- Complete the installation and restart the system if required

---

## 2️⃣ Verify Ollama Installation

After installation, open a terminal or command prompt and run:

```bash
ollama --version
```

# 🧠 Phi Language Model Setup  
## AI Teacher – Local AI Topic Explainer

This document explains how to download, verify, and use the **Phi language model** with **Ollama** for the AI Teacher project.

---

## 📦 About the Phi Model

The **Phi** model is a lightweight large language model optimized for:
- Fast inference
- Low memory usage
- CPU-only systems
- Offline execution

It is ideal for educational tools and local AI applications.

---

## 1️⃣ Download the Phi Model

Use Ollama to download the Phi language model:

```bash
ollama pull phi
```

# 🧠 Phi Language Model – Verification & Usage  
## AI Teacher – Local AI Topic Explainer

This section covers **verification, testing, usage, performance, and limitations** of the **Phi language model** used in the AI Teacher project.

---

## 1️⃣ Verify Phi Model Installation

After downloading the Phi model, verify that it is installed correctly.

### Check Installed Models

Run the following command:

```bash
ollama list
```

## 🧪 Test the Phi Language Model  
### AI Teacher – Local AI Topic Explainer

This section explains how to **test the Phi language model** after installation to ensure it is working correctly.

---

### Start the Phi Model

Run the following command to start an interactive session with the Phi model:

```bash
ollama run phi
```

## 💬 Sample Prompts

- Explain artificial intelligence in simple words  
- What is machine learning?  
- Explain Python libraries  
- Difference between AI and ML  
- Write a Python function to reverse a list  

---


