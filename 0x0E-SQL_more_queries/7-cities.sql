-- Creates a table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id int NOT NULL UNIQUE AUTO_INCREMENT,
       state_id int NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
