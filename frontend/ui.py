
import streamlit as st
from backend.llm_api import query_llm

st.set_page_config(page_title="AI Assistant", page_icon="🤖")

st.title("AI Assistant")
st.caption("Free LLM-based Knowledge Assistant")

prompt = st.text_area("Ask a question")

if st.button("Generate"):
    if not prompt.strip():
        st.warning("Please enter a question")
    else:
        with st.spinner("Generating response..."):
            try:
                answer = query_llm(prompt)
                st.success("Answer")
                st.write(answer)
            except Exception as e:
                st.error("Error communicating with LLM API")
