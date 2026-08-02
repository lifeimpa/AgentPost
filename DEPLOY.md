# Deploy Guide

1. Push to GitHub: initialize repo, add /app files, commit, push.
2. Backend: deploy /backend/ to Render/Heroku (use DATABASE_URL env).
3. Frontend: serve /frontend/index.html via Vercel, Netlify, or Streamlit (python -m streamlit run app.py if wrapping UI).
4. Set env keys: OPENAI_KEY, ANTHROPIC_KEY, DEEPSEEK_KEY, DATABASE_URL, INSTAGRAM_TOKEN.
5. Run: npm install && npm start (backend) + open frontend/index.html or deploy site.

App is ready to download, upload to GitHub, and link to Streamlit or any host.
