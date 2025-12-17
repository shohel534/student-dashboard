import streamlit as st
from pathlib import path

st.set_page_config(
    page_title="student Task Dashboard",
    layout="wide"
)
html_file = path("FDS,.html").read_text(encoding="utf-8")
st.components.v1.html(html_file,height=900,scrolling=True)

