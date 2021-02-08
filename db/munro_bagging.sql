DROP TABLE bags;
DROP TABLE climbers;
DROP TABLE munros;

CREATE TABLE munros (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  height INT
);

CREATE TABLE climbers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE bags (
  id SERIAL PRIMARY KEY,
  climber_id INT REFERENCES climbers(id) ON DELETE CASCADE,
  munro_id INT REFERENCES munros(id) ON DELETE CASCADE,
  review TEXT
);