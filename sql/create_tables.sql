CREATE TABLE IF NOT EXISTS messages1 (
  id SERIAL PRIMARY KEY,
  message_text TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS messages2 (
  id SERIAL PRIMARY KEY,
  message_text TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);