import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_llm(prompt: str) -> str:
    payload = {
        "model": "phi",
        "prompt": f"Answer briefly and clearly:\n{prompt}",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        raise RuntimeError(response.text)

    return response.json()["response"].strip()
