# Why study DB

- the fourth paragidm --> data plays a central role in today's computing
- hard to imagine computing without data today
- it powers a lot of critical services nowadays
- it powers today's computation and AI development


# DBMS

- Database management system
- it's an application that allows you to read and write to DB by parsing sql


# interesting thing

- data-oritented programming


# Schema

- .schema can tell you the statment used to create a table

# Normalizing

- spliting one table (entity) to different tables
- goals: 
-      reduce redundency 
-      one table one type of dataset
-       make the data more efficient
-      beaware of data collision (use uniqe id)

# Storage Class

- NULL
_ INTEGER
  REAL (FLOATING POINT)
  TEXT
  BLOB (binary data)

# Type Affinities

- one column doesn't always store one type of data
- it will try to convert to the appropriate data

# Read from schema
> .read schema.sql

# NO boolean in sqlite

# Table Constrains
- Primary Key
- Foreign Key

# Column constrains

- CHECK
- DEFAULT
- NOT NULL
- UNIQUE

