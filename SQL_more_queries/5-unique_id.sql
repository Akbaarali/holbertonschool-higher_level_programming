-- creates table unique_id with unique id and default value 1

CREATE TABLE IF NOT EXISTS unique_id (
  id INT NOT NULL DEFAULT 1,
  name VARCHAR(256),
  UNIQUE (id)
);
