CREATE DATABASE weather;

USE weather;

CREATE TABLE cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    state VARCHAR(255),
    country VARCHAR(255) NOT NULL
);

CREATE TABLE weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city_id INT NOT NULL,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    pressure FLOAT NOT NULL,
    wind_speed FLOAT NOT NULL,
    wind_direction FLOAT NOT NULL,
    timestamp DATETIME NOT NULL,
    FOREIGN KEY (city_id) REFERENCES cities(id)
);
