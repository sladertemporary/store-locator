DROP TABLE IF EXISTS store;

CREATE TABLE store (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  location TEXT NOT NULL,
  postcode TEXT NOT NULL,
  longitude REAL,
  latitude REAL
);