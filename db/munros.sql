DROP TABLE munros;
DROP TABLE climbers;
DROP TABLE locations;

CREATE TABLE munros (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  height INT,
  duration float
);

CREATE TABLE climbers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
);

CREATE TABLE locations (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  location_id INT REFERENCES locations(id) ON DELETE CASCADE,
  review TEXT
);