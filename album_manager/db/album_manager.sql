DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;


CREATE TABLE artists(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);


CREATE TABLE albums(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    year INT,
    artist_id INT NOT NULL REFERENCES artists(id) ON DELETE CASCADE
);



INSERT INTO artists(first_name,last_name)
VALUES ('A','B');
INSERT INTO artists(first_name,last_name)
VALUES ('A','B');
