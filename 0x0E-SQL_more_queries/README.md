# SQL - Introduction

This project covers introduction to SQL and more queries..
## Learning objectives
This project has satisfy the objectives such as knowing what Database and SQL, basic SQL statememnts (DDL - Data Defining Language and DML - Data Manipulating Language), basic queries (SQL and RA), SQL techniques (functions and sub queries), the difference between backtick and apostrophe, Mysql statement syntax and how to install MySQL IN UBUNTU 20.04.

Below are other topics covered:

* How To Create a New User and Grant Permissions in MySQL
* How To Use MySQL GRANT Statement To Grant Privileges To a User
* MySQL constraints
* SQL technique: subqueries
* Basic query operation: the join
* SQL technique: multiple joins and the distinct keyword
* SQL technique: join types
* SQL technique: union and minus
* MySQL Cheat Sheet
* The Seven Types of SQL Joins
* SQL Style Guide
* MySQL 8.0 SQL Statement Syntax
## Requirements

* Editor: The editor used was vi
* Files were interpreted / compilled on Ubuntu 20.04 LTS using python3
## How to import a SQL dump
```
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
## Author
Olowosuyi Temitope
