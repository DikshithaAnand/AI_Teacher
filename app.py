import streamlit as st
import sys
import os

# -------------------------------------------------
# Ensure project root is in Python path
# -------------------------------------------------
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# Import backend logic
from backend.llm_api import query_llm

# -------------------------------------------------
# Streamlit App Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("AI Assistant")
st.caption("Free LLM-based Knowledge Assistant")

# -------------------------------------------------
# User Input
# -------------------------------------------------
prompt = st.text_area(
    "Ask a question",
    placeholder="Example: Explain the libraries in Python",
    height=120
)

# -------------------------------------------------
# Generate Button
# -------------------------------------------------
if st.button("Generate"):
    if not prompt.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating response..."):
            try:
                answer = query_llm(prompt)
                st.success("Answer")
                st.write(answer)
            except Exception as e:
                # Show real error for debugging
                st.error(str(e))
