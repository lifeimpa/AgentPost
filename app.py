import streamlit as st
st.set_page_config(page_title="AgentPost", layout="wide")
with open("frontend/index.html") as f:
    st.components.v1.html(f.read(), height=900, scrolling=True)
