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

- it's a combination of data from an underlying table so it cannot be updated

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

		```
			CREATE VIEW "2022" AS
			SELECT "id", "title" FROM "books"
			WHERE "year" = 2022;
		```

		```
			CREATE VIEW "2021"
			SELECT "id", "title" FROM "books"
			WHERE "year" = 2021;
		```

	4. Securing

		- hide Personal Identifiable Information (PII)

		```
			SELECT "id", "origin", "destination", "Anonymous" AS "rider"
			FROM "rides";
		```

		- Create a view for that

		```
			CREATE VIEW "analysis" AS
			SELECT "id", "origin", "destination", "Anonymous" AS "rider"
			FROM "rides";
		```
		
		- In Sqlite, we cannot restrict access to table!

**Views Cannot be updated**

- Temp View (of a view)

	```
		CREATE TEMPORARY VIEW "average_ratings_by_year" AS
		SELECT "year", round(avg("ratings"), 2) as "rating" from "avaerage_book_ratings"
		group by "year";
	```

	- it will be gone after quiting the sqlite terminal

- CTE (common table expression)

	- A temporary view that exists only within the duration of a query
	- used only for querying

	```
		WITH name AS (
			SELECT ...
		), ...
		SELECT ... FROM name
	```

	- Example

		```
			WITH "avarage_book_ratings" AS (
				CREATE VIEW "average_book_ratings" AS
				SELECT "book_id", "title", "year",  ROUND(AVG("rating"), 2) AS "rating"
				FROM "ratings"
				JOIN "books" on "ratings"."book_id" = "books"."id"
				GROUP BY "ratings"."book_id"
			)
			SELECT "year", ROUND(AVG("rating"), 2) AS "rating"
			FROM "avarage_book_ratings"
			GROUP BY "year";
		```
	
- Drop View

	```
		DROP VIEW name
	```

- Soft Deletion

	```
		CREATE VIEW "current_collections" AS
		SELECT "id", "title", "accession_number", "acquired"
		FROM "collections" WHERE "delected" != 1;
	```

- Views cannot be modified, but the underlying table can

- Use triggers to update view (modifying the underlying table)

	```
		CREATE TRIGGER name
		INSTEAD OF DELETE ON view_name
		FOR EACH ROW
		BEGIN
			...;
		END;
	```

	- Example

		```
			CREATE TRIGGER "delete"
			INSTEAD OF DELETE ON "current_collections"
			FOR EACH ROW
			BEGIN
				UPDATE "collections" SET "deleted" = 1
				WHERE "id" = OLD."id";
			END;
		```
- Use triggers to insert data on view with condition

	```
		CREATE TRIGGER "insert_when_exists"
		INSTEAD OF INSERT ON "current_collections"
		FOR EACH ROW
		WHEN NEW."accession_number" IN (
			SELECT "accession_number" FROM "collections"
		)
		BEGIN
			UPDATE "collextions" SET "deleted" = 0
			WHERE "accession_number" = NEW."accession_number";
		END;
	```
## Optimizing

- profiling query

	```
	.timer on
	```

- real time

	- clock time

- user time

	- time it took CPU to execute the query

- sys time

	- time it takes for system to wait to run the query

- Index

	- A structure used to speed up the retrieval of rows from a table

	```
	CREATE INDEX name 
	ON TABLE (column0, ...);
	```

	```
	DROP INDEX "index_name"; 
	```

	- using index can make a query 70 times faster!

- Explain Query Plan

	```
	EXPLAIN QUERY Plan
	(Query)
	```
- Covering Index

	- An index in which queried data can be retrieved from the index itself without going to the table

- Notes on Index

> Index can take up space (trade off for speed)

- B-Tree (Data structure)

	- A balanced tree
	- used to create an index in DB
	- inserting can be a hassle

**Optimising for Space**

- Partial Index

	- An index that includes only a subset of rows from a table

```
CREATE INDEX name
ON table (column0...)
WHERE condition;
```

- Vacuum

```
du -b file -> check bytes used
```

```
VACUUM;
```

- when you delete it, it's just marked as de-allocated (can be traced back)
- the way to give back the memory to the system




