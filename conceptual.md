### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL is an advanced, enterprise class open source relational database that supports both SQL (relational) and JSON (non-relational) querying.

- What is the difference between SQL and PostgreSQL?
SQL server is a database management system which is mainly used for e-commerce and providing different data warehousing solutions. PostgreSQL is an advanced version of SQL which provides support to different functions of SQL like foreign keys, subqueries, triggers, and different user-defined types and functions.

- In `psql`, how do you connect to a database?
you need to know the name of your target database, the host name and port number of the server, and what user name you want to connect as. psql can be told about those parameters via command line options, namely -d, -h, -p, and -U respectively.

- What is the difference between `HAVING` and `WHERE`?
A HAVING clause is like a WHERE clause, but applies only to groups as a whole (that is, to the rows in the result set representing groups), whereas the WHERE clause applies to individual rows. A query can contain both a WHERE clause and a HAVING clause.

- What is the difference between an `INNER` and `OUTER` join?
he biggest difference between an INNER JOIN and an OUTER JOIN is that the inner join will keep only the information from both tables that's related to each other (in the resulting table

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
A left outer join contains all records of the "left" table even if it has no matches in the "right" table specified in the join. A right outer join contains all records in the "right" able even if it has no matches in the "left" table. A full outer join contains all records of both the left and right tables.

- What is an ORM? What do they do?
s a technique used in creating a "bridge" between object-oriented programs and, in most cases, relational databases.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
AJAX is a way of using HTTP1 where the never changing parts of a website (i.e. some html and the javascript files2) are separated from the changing data.

- What is CSRF? What is the purpose of the CSRF token?
to prevent CSRF attacks.

- What is the purpose of `form.hidden_tag()`?
generates a hidden field that includes a token that is used to protect the form against CSRF attacks