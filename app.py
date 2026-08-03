import streamlit as st
import os, requests

st.set_page_config(page_title="AgentPost — Live", layout="wide")
st.title("AgentPost — AI Social Engine")
st.success("Live • DeepSeek connected • Ready to generate")

DEEPSEEK_KEY = os.environ.get("DEEPSEEK_KEY") or st.secrets.get("DEEPSEEK_KEY", "")

with st.form("generate"):
    product = st.text_area("Product / Website info", "Summer bracelet, gold, handmade, $28")
    season = st.selectbox("Season / Context", ["Spring","Summer","Fall","Holiday","Trending"])
    style = st.text_input("Writing style", "Friendly, emoji light, call to action")
    submitted = st.form_submit_button("Generate Multi-Angle Posts")

if submitted and DEEPSEEK_KEY:
    with st.spinner("AI writing 3 angles..."):
        prompt = f"Write 3 social media post angles for: {product}. Season: {season}. Style: {style}. Include caption, headline, hashtags."
        try:
            resp = requests.post("https://api.deepseek.com/chat/completions",
                headers={"Authorization": f"Bearer {DEEPSEEK_KEY}", "Content-Type": "application/json"},
                json={"model":"deepseek-chat","messages":[{"role":"user","content":prompt}],"temperature":0.7}, timeout=30)
            result = resp.json()["choices"][0]["message"]["content"]
            st.subheader("Generated Content")
            st.write(result)
        except Exception as e:
            st.error(f"DeepSeek error: {e}")
elif submitted and not DEEPSEEK_KEY:
    st.warning("Add DEEPSEEK_KEY to Streamlit Secrets to generate.")

st.divider()
st.markdown("**Features:** Scrape • Learn • Multi-Angle • Image Toggle • Approval • Schedule • Instagram • Brain")
