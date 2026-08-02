import streamlit as st
st.set_page_config(page_title="AgentPost", layout="wide")
st.title("AgentPost — AI Social Publishing Engine")
st.markdown("""
**Standalone SaaS** — Scrape site, learn season/style, write multi-angle posts,
use real or AI images, approve/edit, schedule/batch, post to 6 platforms.

Features: Scraper • Season Engine • Style Learning • Multi-Angle Writer • 
Image Toggle (Real / AI) • Approval Flow • Scheduling • Instagram Trigger • 
Brain / Suggestions • Mobile PWA
""")
with open("frontend/index.html") as f:
    st.components.v1.html(f.read(), height=800, scrolling=True)
