# Universal Deploy (Any Host)
1. Push /app/ to GitHub
2. Any host with Docker: `docker build -t agentpost .` && `docker run -p 8000:8000 agentpost`
3. Or use Render / Railway / DigitalOcean: connect repo, set Dockerfile, deploy.
4. Set env vars (DB, API keys) in host dashboard.
Works everywhere — not locked to Streamlit.
