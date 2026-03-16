import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ResumeAI Pro",
    layout="wide"
)

st.title("ResumeAI Pro — Intelligent Resume & Career Platform")

# Read the HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render HTML inside Streamlit
components.html(html_content, height=1200, scrolling=True)
