# 🤖 AI Teacher – Local AI Topic Explainer

AI Teacher is a **local, offline AI-powered topic explainer** built using **Streamlit** and **Ollama**.  
It uses a lightweight **Phi language model** to generate fast and clear explanations without relying on cloud APIs or internet access after setup.

This project is suitable for **learning, internships, mini projects, and demonstrations**.

---

## 🚀 Features

- 🧠 Local AI model (no cloud or API keys)
- ⚡ Fast responses optimized for CPU
- 🔒 Secure (no secrets or tokens required)
- 🌐 Works offline after setup
- 🧑‍🎓 Ideal for explaining topics and concepts
- 💻 Simple and clean Streamlit interface

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **LLM:** Phi model  
- **Inference Engine:** Ollama (local HTTP Api)

---

## 📁 Project Structure
```text
ai-assistant/
│
├── app.py
├── backend/
│ ├── init.py
│ └── llm_api.py
│
├── frontend/
├── requirements.txt
├── .gitignore
└── README.md
```
---

## ⚙️ Installation & Setup

### 1️⃣ Install Ollama
Download from:
https://ollama.com/download

Verify installation:
```bash
ollama --version
```

## 2️⃣ Install Phi Model

Download the lightweight Phi language model using Ollama:

```bash
ollama pull phi
```

## 3️⃣ Create Virtual Environment (Optional)

It is recommended to use a virtual environment for dependency management.

```bash
python -m venv venv
venv\Scripts\activate
```

## 4️⃣ Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## 5️⃣ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

# 🧪 Example Prompts

You can ask the AI Assistant the following types of questions:

- Explain the libraries in Python  
- What is machine learning?  
- Explain India’s economy in simple terms  
- Write a Python function to reverse a list  

These prompts demonstrate the system’s ability to explain concepts and generate simple code snippets.

---

# ⚡ Performance Notes

- Uses the **Phi language model (~1.6 GB)** for fast inference  
- Runs completely **offline** after initial setup  
- The model is kept **in memory** using Ollama’s local server  
- Optimized for **CPU-only systems**, suitable for laptops and low-resource machines  

This design ensures low latency and consistent performance.

---

# 🎓 Use Cases

- Topic explanation tool for students  
- Offline AI-based learning assistant  
- Internship or academic mini project  
- Demonstration of AI fundamentals and local LLM deployment  

The project is suitable for both educational and demonstrative purposes.

# ⚠️ Limitations

- Knowledge cutoff depends on the model training data (approximately 2023)  
- Does not provide real-time or live internet-based information  
- Designed mainly for explanations, not large-scale or production applications.

These limitations are expected for local, offline language models.

# 📌 Future Enhancements

- Add a model selector (Phi / Mistral)  
- Introduce an Explanation vs Code output toggle  
- Implement chat history support  
- Improve UI design and theming  
- Add options to export or save responses  

These enhancements can further improve usability and functionality.

## 👤 Author

**Dikshitha Anand**

- AI & Machine Learning Enthusiast  
- Interested in Python, Data Structures, and AI-based applications  
- Focused on building practical AI tools using open-source technologies

**GitHub:** https://github.com/DikshithaAnand

---

