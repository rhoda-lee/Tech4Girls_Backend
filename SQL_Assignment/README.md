# MANAGING DATABASES WITH MySQL: SQL ASSIGNMENT

![Header Image](./header-image.jpg)

A Database is a structured or unstructured collection of data that the backend server 
uses to store and manage informatio efficiently.
A  database can be accessed by the backend code to retrieve, update and delete data
updating, and deletion of data, helping applications to function smoothly.
Databases can store information in tables, rows and columns, 
ensuring that data is organized and easily accessible.

SQL (Structured Query Language) is a query language used to communicate 
with relational databases. It is used for querying, updating, inserting 
and deleting data in a database. SQL provides commands such as SELECT, 
INSERT, UPDATE and DELETE which are used to interact with the data.

MySQL is a popular open-source relational database management system (RDBMS) that uses SQL to manage data. It is widely used for storing data in web applications and other systems, offering features such as high performance, security and scalability. MySQL allows developers to create, modify and query databases efficiently, making it a fundamental tool for backend development.


## Author
* [Rhoda Oduro-Nyarko](https://github.com/rhoda-lee)


## Submission Overview: SQL Assignmemt
This repository contains SQL code for an assignment to gain practical exposure to managing data using relational database:
1. Create a Database
2. Use a Database
3. Create a Table
4. Insert Values into the Table
5. Select all table columns and rows
6. Establish a One-to-Many relationship between the tables by referencing a colun in another table
7. Establish a Many-to-Many relationship between tables using foreign keys

The project is structured to help us understand essential database fundamental
concepts such as creating and using a database, creating a table, inserting values,
selecting table and modifying values like deleting and updating a table. 

It also helps us better understand and know how to establish relationships between tables in adatabase by referencing a column in another table as a Foreign Key.

## How to Use This Repository

```bash
  #Clone the repository to your local machine.
  git clone https://github.com/rhoda-lee/Tech4Girl_Backend.git

  #Navigate to the directory where you cloned it.
  cd SQL_Assignment 

  #Run the provided SQL scripts in your terminal.
   mysql -u -root -p < sql_script_name.sql

  #Follow the prompts in each script to interact with the programs.
```


## Submission Structure
The submission contains the following files and directories:

* **question1.sql**: Creates a database and inserts values into a table
* **question2.sql**: Creates a table, establishing a one-to-many relationship between the table in question1.sql and the table in this file
* **question3.sql**: Creates a table, establishing a many-to-many relationship between the table in question1.sq2 and the table in this file

Objectives:
* Create a Database and Use it
* Create tables and insert values into them
* Establish relationships between tables using foreign keys

## Aspects
* Database Creation: 
  - Creates a Database in the question1.sql script
  ```bash
  CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;
  ```
* Table Creation:
  - Creates a Table in the sql scripts
  ```bash
  CREATE TABLE IF NOT EXISTS Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
  ```
* Inserting values into Tables:
  - Inserts table values in the scripts
  ```bash
  -- ISERTING VALUES INTO THE USERS TABLE
  INSERT INTO Users (username, email)
  VALUES ('Ama', 'ama@example.com'),
  ('Abena', 'abena@example.com'),
  ('Ajoa', 'adjoa@example.com');
  ``` 
* Selecting all columns and rows in a table: 
  - Selects all the columns and rows in a table
 ```bash
  SELECT * FROM Users;
 ```
* Foreign keys to establish relationships: 
  - Establishing a relationship between the Users and Posts table using foreign keys
```bash
-- CREATING THE POSTS TABLE
CREATE TABLE IF NOT EXISTS Posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
  

## Tech Stack
* SQL
    - MySQL

