# 🤖 AI Teacher – Local Offline AI Learning Assistant

AI Teacher is a lightweight offline AI-powered educational assistant developed using **Python, Streamlit, and Ollama**.  
The application uses the **Phi Large Language Model** to generate fast, interactive, and easy-to-understand topic explanations directly on a local machine.

Unlike cloud-based AI systems, AI Teacher works completely offline after setup, eliminating the need for external APIs, subscriptions, or continuous internet access.

---

# 🌟 Project Overview

AI Teacher is designed to demonstrate how modern AI systems can run locally with minimal resources while maintaining speed, privacy, and usability.

The project focuses on:
- Offline AI inference
- Educational topic explanation
- Lightweight local LLM deployment
- Beginner-friendly interaction
- Secure AI execution without cloud dependency

This project is suitable for:
- Students
- Academic mini-projects
- Internship portfolios
- AI demonstrations
- Local LLM experimentation

---

# ✨ Key Features

- 🧠 Fully offline AI assistant
- ⚡ Fast topic explanation using Phi model
- 🔒 No API keys or cloud services required
- 💻 Simple and clean Streamlit interface
- 🌐 Works locally after installation
- 📚 Educational and beginner-friendly
- 🛠️ Easy to customize and extend
- 🤖 Lightweight local LLM integration
- 🔍 Interactive question-answer system

---

# 🚀 Technologies Used

## Frontend
- Streamlit

## Backend
- Python

## AI Model
- Phi Language Model

## Local Inference Engine
- Ollama

---

# 📂 Project Structure

```text
ai-teacher/
│
├── app.py
├── backend/
│   ├── __init__.py
│   └── llm_api.py
│
├── frontend/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ System Requirements

Before installing the project, ensure your system meets the following requirements:

- Python 3.9 or higher
- Minimum 4 GB RAM recommended
- Internet connection for initial setup only
- Windows / Linux / macOS supported

---

# ⚙️ Installation Guide

## 1️⃣ Install Ollama

Download Ollama from the official website:

```bash
https://ollama.com/download
```

Install the appropriate version for your operating system.

---

## 2️⃣ Verify Ollama Installation

Open terminal or command prompt and run:

```bash
ollama --version
```

If installed correctly, the Ollama version will be displayed.

---

# 🧠 Phi Model Setup

## Download the Phi Model

Run the following command:

```bash
ollama pull phi
```

This downloads the Phi language model locally.

---

## Verify Installed Models

```bash
ollama list
```

You should see the Phi model listed.

---

# 🧪 Testing the Phi Model

Start the model using:

```bash
ollama run phi
```

You can now interact with the AI model locally.

---

# 💬 Example Prompts

```text
Explain Artificial Intelligence in simple words
What is Machine Learning?
Difference between AI and Deep Learning
Explain Python libraries
Write a Python program to reverse a list
```

---

# ▶️ Running the Application

Install required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

# 🎯 Project Objectives

- Demonstrate offline AI execution
- Build a practical educational assistant
- Explore local Large Language Models
- Create a lightweight AI learning platform
- Understand local inference using Ollama

---

# 📈 Future Improvements

- Voice input and output support
- Multi-language explanations
- AI-generated quizzes
- Chat history management
- PDF/document summarization
- Dark mode interface
- Custom fine-tuned models

---

# 🧑‍💻 Author

## Dikshitha Anand
Student Developer | AI & Machine Learning Enthusiast

### Areas of Interest
- Artificial Intelligence
- Machine Learning
- NLP & LLMs
- Python Development
- Local AI Systems
- Backend Development

### GitHub
```bash
https://github.com/DikshithaAnand
```

---

# 📌 Conclusion

AI Teacher demonstrates that powerful AI educational systems can run efficiently on local machines without relying on expensive cloud infrastructure.

The project combines simplicity, privacy, and practical AI implementation, making it an excellent learning project for students and developers exploring local LLM applications.

---
