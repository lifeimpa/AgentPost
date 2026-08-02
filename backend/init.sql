CREATE TABLE users (id SERIAL PRIMARY KEY, email, name, created_at);
CREATE TABLE stores (id SERIAL PRIMARY KEY, user_id, url, name);
CREATE TABLE products (id SERIAL PRIMARY KEY, store_id, name, price, image_url, description);
CREATE TABLE drafts (id SERIAL PRIMARY KEY, user_id, store_id, product_id, caption, angle, status, created_at);
CREATE TABLE approvals (id SERIAL PRIMARY KEY, draft_id, user_id, decision, edited_caption, edited_at);
CREATE TABLE schedules (id SERIAL PRIMARY KEY, draft_id, platform, post_time, status);
CREATE TABLE social_accounts (id SERIAL PRIMARY KEY, user_id, platform, token, refreshed_at);
CREATE TABLE ai_configs (id SERIAL PRIMARY KEY, user_id, provider, api_key_encrypted, active);
CREATE TABLE suggestions (id SERIAL PRIMARY KEY, user_id, type, content, approved, created_at);
