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

# Insert

`
	INSERT INTO TABLE (column name)
	VALUES (val1...), (val2...) ...;
`
- id is not required when inserting

# Import

.import --csv --skip 1 <file_name>;

# Import using temp

- .import --csv mfa.csv temp

`
	INSERT INTO table (col1, col2 ...) 
	SELECT  (col1, col2 ...) FROM "table2"; 
`

- Import from CSV treat everything as string, so no NULL

- sqlite treat 'yyyy-mm-dd' as a proper datestring format

# Foreign Key Constraint

- Delete foreign key association first

- FOREIGN KEY ... ON DELETE RESTRICT / NO ACTION / SET NULL / CASCADE

# Deleted id

- if id is set to AUTO_INCREMEN, it will reuse the delete id!

# update 

`
	UPDATE table SET col = ...
	WHERE condition;

`

# SQL Trim

- trim("col")

# SQL Upper
- upper("col")

# SQL like
- it's case insenstive

# Trigger

- used for a log
- a sql statement executed before or after some other statement

`
	CREATE TRIGGER name
	BEFORE / AFTER DELETE ON table
	FOR EACH ROW
	BEGIN
		...;
	END;

`

# Soft Delection

- using a deleted column to soft delete

# View in SQL

- a virtual table defined by a query

- it won't use much disk space since it's only a virtual table

# Usage of View

	1. Simplifying
		
		- From

			```
				SELECT "title" FROM "books"
				WHERE "id" IN (
					SELECT "book_id" FROM "authored"
					WHERE "author_id" = (
				        SELECT "id" FROM "authors"
					    WHERE "name" = 'Frenanda Melchor'
					)
				);
			```

		- To

			```
				CREATE VIEW "longlist" AS
				SELECT "name", "title" FROM "authors"
				JOIN "authored" on "authors"."id" = "authored"."author_id"
				JOIN "books" on "books"."id" = "authored"."book_id";
			```

		- Then

			```
				SELECT "title" FROM "longlist"
				WHERE "name" = 'Frenanda Melchor';
			```

	2. Aggregating

		- From

			```
				SELECT "book_id", "title", "year",  ROUND(AVG("rating"), 2) AS "rating"
				FROM "ratings"
				JOIN "books" on "ratings"."book_id" = "books"."id"
				GROUP BY "ratings"."book_id";
			```

		- To 

			``` 
				CREATE VIEW "average_book_ratings" AS
				SELECT "book_id", "title", "year",  ROUND(AVG("rating"), 2) AS "rating"
				FROM "ratings"
				JOIN "books" on "ratings"."book_id" = "books"."id"
				GROUP BY "ratings"."book_id";
			```
	3. Partioning
	4. Securing
