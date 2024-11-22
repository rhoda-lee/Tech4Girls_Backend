-- Question 1

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

-- ISERTING VALUES INTO THE USERS TABLE
INSERT INTO Users (username, email)
VALUES ('Ama', 'ama@example.com'),
('Abena', 'abena@example.com'),
('Ajoa', 'adjoa@example.com');

-- OUTPUT
/* mysql> SELECT * FROM Users;
+----+----------+-------------------+---------------------+
| id | username | email             | created_at          |
+----+----------+-------------------+---------------------+
|  1 | Ama      | ama@example.com   | 2024-11-22 10:16:49 |
|  2 | Abena    | abena@example.com | 2024-11-22 10:16:49 |
|  3 | Ajoa     | adjoa@example.com | 2024-11-22 10:16:49 |
+----+----------+-------------------+---------------------+
3 rows in set (0.00 sec) */
