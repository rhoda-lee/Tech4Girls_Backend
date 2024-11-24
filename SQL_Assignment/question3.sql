-- Question3

-- QUERY TO SELECT AND USE A DATABASE - WE ARE USING THE Tech4Girls_DB
USE Tech4Girls_DB;

-- CREATING A TABLE CALLED Courses
CREATE TABLE IF NOT EXISTS Courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);


-- CREATING ANOTHER TABLE CALLED User_Courses
CREATE TABLE IF NOT EXISTS User_Courses (
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES  Users(id),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

-- QUERY TO SHOW THAT TABLES HAVE BEEN CREATED IN OUR DATABASE
SHOW TABLES;

-- OUTPUT
/*mysql> SHOW TABLES;
+-------------------------+
| Tables_in_Tech4Girls_DB |
+-------------------------+
| Courses                 |
| Posts                   |
| User_Courses            |
| Users                   |
+-------------------------+
4 rows in set (0.01 sec) */

-- INSERTING VALUES INTO THE Courses TABLES
INSERT INTO Courses (course_name)
VALUES('Operating Systems'),
('Database Fundamentals'),
('Principles of 3D Environment'),
('Software Engineering');

-- SELECTING ALL COLUMNS AND ROWS IN THE Courses TABLE TO BE DISPLAYED
SELECT * FROM Courses;

-- OUTPUT
/* mysql> SELECT * FROM Courses;
+----+------------------------------+
| id | course_name                  |
+----+------------------------------+
|  1 | Operating Systems            |
|  2 | Database Fundamentals        |
|  3 | Principles of 3D Environment |
|  4 | Software Engineering         |
+----+------------------------------+
4 rows in set (0.00 sec) */

-- INSERTING VALUES INTO THE User_Courses TABLES
INSERT INTO User_Courses (user_id, course_id)
VALUES (1, 2),
(1, 4),
(3, 1),
(2, 2),
(2, 1),
(3, 4),
(2, 3);

/* Both the user_id and the course_id are Integers so we will pass whole nummbers
These numbers we pass represent a user's id and the id of a particular course
The User_Courses table establishes a Many-to-Many relationship between the Courses and Users table
such that, each user can register for multiple courses. Each course can be selected once by a specific user
Each course is offered by many users.
So user by id (1) can offer course by id(4) at the same time offer course by id (3), ie: (1,4), (1,4)
So course by id (3) can be offered by user with id(2) 
at the same time the course can be offered by user with id(3) ie: (3,2), (3,3) */

-- SELECTING ALL COLUMNS AND ROWS IN THE Users TABLE TO BE DISPLAYED
SELECT * FROM Users;

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

-- SELECTING ALL COLUMNS AND ROWS IN THE User_Courses TABLE TO BE DISPLAYED
SELECT * FROM User_Courses;

-- OUTPUT
/* mysql> SELECT * FROM User_Courses;
+---------+-----------+
| user_id | course_id |
+---------+-----------+
|       1 |         2 |
|       1 |         4 |
|       3 |         1 |
|       2 |         2 |
|       2 |         1 |
|       3 |         4 |
|       2 |         3 |
+---------+-----------+
7 rows in set (0.00 sec) */