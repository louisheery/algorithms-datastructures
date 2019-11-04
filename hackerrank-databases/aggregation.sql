-- Revising Aggregations - The Count Function
SELECT COUNT(NAME) FROM CITY WHERE POPULATION > 100000

-- Revising Aggregations - The Sum Function
SELECT SUM(POPULATION) FROM CITY WHERE DISTRICT = "California"

-- Revising Aggregations - Averages
SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = "California"

-- Average Population
SELECT ROUND(AVG(POPULATION), 0) FROM CITY

-- Japan Population
SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE = "JPN"

-- Population Density Difference
SELECT MAX(POPULATION) - MIN(POPULATION) FROM CITY

-- Top Earners
SELECT MAX(months * salary), count(employee_id) FROM employee WHERE (months * salary) = (SELECT MAX(months * salary) FROM employee);

-- Weather Observation Station 2
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2) FROM STATION

-- Weather Observation Station 13
SELECT ROUND(SUM(LAT_N), 4) FROM STATION WHERE LAT_N > 38.7880 AND LAT_N < 137.2345

-- Weather Observation Station 14
SELECT ROUND(MAX(LAT_N), 4) FROM STATION WHERE LAT_N < 137.2345

-- Weather Observation Station 15
SELECT ROUND(LONG_W, 4) FROM STATION WHERE LAT_N = (SELECT MAX(LAT_N) FROM STATION WHERE LAT_N < 137.2345)

-- Weather Observation Station 16
SELECT ROUND(MIN(LAT_N),4) FROM STATION WHERE LAT_N > 38.7780

-- Weather Observation Station 17
SELECT ROUND(LONG_W, 4) FROM STATION WHERE LAT_N = (SELECT MIN(LAT_N) FROM STATION WHERE LAT_N > 38.7780)

-- Weather Observation Station 18
SELECT ROUND((MAX(LONG_W) - MIN(LONG_W)) + (MAX(LAT_N) - MIN(LAT_N)), 4) FROM STATION

-- Weather Observation Station 19
SELECT ROUND(SQRT(POWER(MAX(LAT_N) - MIN(LAT_N), 2) + POWER(MAX(LONG_W) - MIN(LONG_W), 2)), 4) FROM STATION
