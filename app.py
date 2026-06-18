import streamlit as st
from agent import agent

st.set_page_config(
    page_title="Baseball Fantasy Agent",
    page_icon="⚾",
    layout="centered",
)

st.title("⚾ Baseball Fantasy Agent")
st.caption(
    "Ask about player stats, splits, and start/sit decisions to give you a Fantasy advantage. "
    "Powered by smolagents, the MLB Stats API, and a local LLM via Ollama."
)

with st.form("query_form"):
    question = st.text_input(
        "Your question",
        placeholder="How does Aaron Judge perform against left-handed pitchers?",
    )
    submitted = st.form_submit_button("Ask")

if submitted and question:
    with st.spinner("Analyzing..."):
        response = agent.run(question)
    st.markdown(response)
elif submitted and not question:
    st.warning("Please enter a question.")