-- Database setup
CREATE DATABASE covid_db;
USE covid_db;

-- Table creation
CREATE TABLE covid_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(100),
    date DATE,
    total_cases INT,
    total_deaths INT,
    total_vaccinations INT
);

-- Example query: Deaths by country
SELECT country, SUM(total_deaths) AS deaths
FROM covid_data
GROUP BY country
ORDER BY deaths DESC;

-- Example query: Vaccination progress
SELECT country, MAX(total_vaccinations) AS vaccinations
FROM covid_data
GROUP BY country
ORDER BY vaccinations DESC;
