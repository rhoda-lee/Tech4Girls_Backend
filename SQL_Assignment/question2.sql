-- Start of Question 1

-- CREATING Tech4Girls_DB Database
CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;

-- SHOWING DATABASES
SHOW DATABASES;

-- USING THE DTABASE
USE Tech4Girls_DB;

-- CREATING USERS TABLE IN THE Tech4Girls_DB Database
CREATE TABLE IF NOT EXISTS Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SHOW TABLES;

-- ISERTING VALUES INTO THE USERS TABLE
INSERT INTO Users (username, email)
VALUES ('Ama', 'ama@example.com'),
('Abena', 'abena@example.com'),
('Ajoa', 'adjoa@example.com');

-- SELECTING ALL COLUMNS AND ROWS IN THE USERS TABLE TO BE DISPLAYED
SELECT * FROM Posts;

-- End of Question 1




-- QUESTION2 

-- USING THE Tech4Girls_DB DATABASE
USE Tech4Girls_DB;

-- CREATING THE POSTS TABLE
CREATE TABLE IF NOT EXISTS Posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SHOW TABLES;

-- INSERTING INTO Posts TABLE TO ESTABLISH ONE-TO-MANY RELATIONSHIP
INSERT INTO Posts (user_id, title, content)
VALUES (1, 'Into the Unknown', 'I slowly drift into a world unfamiliar, a world where I have so much yet so little control over.'),
(2, 'Tranquility', 'The winds of sleep tug at my very eyes, urging me to sleep and not to rise.'),
(2, 'Resilience', 'I came, I saw, I conqured!'),
(3, 'Letter to myself', 'You have come so far. You are doing amazing'),
(1, 'Life', 'The more I learn, the more I realize how much I do not know!');

-- SELECTING ALL COLUMNS AND ROWS IN THE POSTS TABLE TO BE DISPLAYED
SELECT * FROM Posts;

-- Output
/*
+----+---------+------------------+--------------------------------------------------------------------------------------------------+---------------------+
| id | user_id | title            | content                                                                                          | created_at          |
+----+---------+------------------+--------------------------------------------------------------------------------------------------+---------------------+
|  1 |       1 | Into the Unknown | I slowly drift into a world unfamiliar, a world where I have so much yet so little control over. | 2024-11-24 20:55:57 |
|  2 |       2 | Tranquility      | The winds of sleep tug at my very eyes, urging me to sleep and not to rise.                      | 2024-11-24 20:55:57 |
|  3 |       2 | Resilience       | I came, I saw, I conqured!                                                                       | 2024-11-24 20:55:57 |
|  4 |       3 | Letter to myself | You have come so far. You are doing amazing                                                      | 2024-11-24 20:55:57 |
|  5 |       1 | Life             | The more I learn, the more I realize how much I do not know!                                     | 2024-11-24 20:55:57 |
+----+---------+------------------+--------------------------------------------------------------------------------------------------+---------------------+
5 rows in set (0.00 sec) */
