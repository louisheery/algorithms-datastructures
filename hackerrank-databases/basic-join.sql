-- Asian Population
SELECT SUM(CITY.POPULATION) FROM CITY JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.CONTINENT = "Asia"

-- African Cities
SELECT CITY.NAME FROM COUNTRY JOIN CITY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = "Africa"

-- Average Population of Each Continent
SELECT COUNTRY.Continent, ROUND(AVG(CITY.Population)-0.5) FROM COUNTRY JOIN CITY ON COUNTRY.CODE = CITY.COUNTRYCODE
GROUP BY COUNTRY.Continent
ORDER BY AVG(CITY.Population) ASC

-- The Report
SELECT students.name, grades.grade, students.marks FROM STUDENTS JOIN GRADES ON Students.marks BETWEEN grades.min_mark and grades.max_mark
WHERE grades.grade >= 8
ORDER BY grades.grade DESC, students.name ASC;


SELECT Null, grades.grade, students.marks FROM STUDENTS JOIN GRADES ON Students.marks BETWEEN grades.min_mark and grades.max_mark
WHERE grades.grade < 8
ORDER BY grades.grade DESC, students.name ASC;

-- Top Competitors
SELECT hackers.hacker_id, hackers.name
FROM submissions JOIN challenges
ON submissions.challenge_id = challenges.challenge_id

JOIN difficulty on challenges.difficulty_level = difficulty.difficulty_level

JOIN hackers on submissions.hacker_id = hackers.hacker_id

WHERE submissions.score = difficulty.score
    AND challenges.difficulty_level = difficulty.difficulty_level

GROUP BY hackers.hacker_id, hackers.hacker_id, name
    HAVING COUNT(submissions.hacker_id) > 1

ORDER BY COUNT(submissions.hacker_id) DESC, submissions.hacker_id ASC
