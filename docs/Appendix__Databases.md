# Appendix: Databases
Knex.Js officially supports the following databases:
- PostgreSQL
- MariaDB
- MySQL
- Oracle
- SQLite
- Amazon Redshift

Here, we are comparing MySQL/MariaDB (they are nearly the same), SQLite, and PostgreSQL.

## Relational Database comparison
### SQLite
The SQLite project’s website describes it as a “serverless” database. This means that any process that accesses the database are reads and writes directly to the disk file, without the need for a database engine, compared to MySQL and PostgreSQL. This simplifies SQLite’s setup process, since it eliminates any need to configure a server process. Likewise, there’s no configuration necessary for programs that will use the SQLite database: all they need is access to the disk. This serverless architecture enables the database to be cross-platform compatible. SQLite is used for Android & iOS Mobile phones but also for McAfee antivirus programs, Skype program for Mac OSX and Windows, Firefox...

##### Advantages
SQLite is a good choice for low-to-medium traffic websites (~100k requests a day) due to its small footprint (600kb of space), user setup friendly, and portability.

##### Disadvantages
Although multiple processes can **access** and **query** an SQLite database at the same time, only one process can make **changes** to the database at any given time.
This puts SQLite at a disadvantage to MySQL and PostgreSQL when working with lots of data or high write volumes.

### MySQL
MySQL has been the most popular open-source RDBMS for websites in the past years, which powers many of the world’s largest websites and applications, including Twitter, Facebook, Netflix, and Spotify. 
Getting started with MySQL is relatively straightforward, thanks in large part to its exhaustive documentation and a large community of developers, as well as the abundance of MySQL-related resources online.

MySQL was designed for speed and reliability at the expense of fully complying with the SQL standards. The MySQL developers continually work towards closer adherence to standard SQL, but it still lags behind other SQL implementations.

In 2008, *Sun Microsystems* acquired MySQL. 2 years later, MariaDB, a fork (a copy) of MySQL emerged because developers were not happy with the for-profit policy of *Sun Microsystems*. Both continue to work the same way.
*Opinionated statement: MariaDB can be seen as the real "2008 MySQL" successor.* 

##### Advantages
MySQL is a good choice for all kind of websites due to its popularity and ease of use, improved security (compared to SQLite), speed (by choosing not to implement certain SQL features) and the ability of database replication which is the practice of sharing information across two or more hosts (multiple databases on multiple computers) to help improve reliability, availability, and fault-tolerance

##### Disadvantages
MySQL, however, is known with certain SQL limitations, such as lacking support for `FULL JOIN` clauses. Also, if your application has lots of users writing data to it at once, another RDBMS like PostgreSQL might be a better choice of database (e.g., a chat application if it needs to be an SQL database).

### PostgreSQL
PostgreSQL, also known as Postgres, bills itself as “the most advanced open-source relational database in the world.” It was created to be highly extensible and SQL standards-compliant.

Postgres is capable of efficiently handling multiple tasks at the same time, a characteristic known as concurrency, **but** don't let this blind you as if PostgreSQL is more performant than MySQL (have a look at advantages/disadvantages). It achieves this without reading locks thanks to its implementation of Multiversion Concurrency Control (MVCC), which ensures the atomicity, consistency, isolation, and durability of its transactions, also known as ACID compliance (FYI: SQLite and MySQL are also ACID compliant).

##### Advantages
PostgreSQL is a good choice for all kinds of websites for the same reasons as MySQL but additionally handles multi-user environments much better and has built-in support for JSON and Array data types.

##### Disadvantages
When compared to MySQL, PostgreSQL is more power-hungry, as it takes up 10MB RAM for each client connection. This model can take up much memory as concurrent client connection goes when compared to the thread-per-connection model of MySQL. Another big disadvantage can be seen during frequent UPDATEs, where due to no support for clustered indexes, PostgreSQL can have a huge adverse impact on performance compared to MySQL databases.


### Which to pick?
Thanks to Knex.Js query methods, we don't have to think that much about database-specific syntaxes. We can switch between SQL databases in no time without having to rewrite code.

**But** the database behind a web application matters. SQLite should be used for single-user websites. 
Later on, when you have to build production-ready websites with multiple functionalities and users, then you should switch to MySQL or PostgreSQL.

MySQL and PostgreSQL are both excellent choices, and you should pick the one you're most comfortable with and used to. Many online platforms discuss which is better - but both are performant, one over the other depending on the operation.

Personally, if you are new to databases, go with MySQL since it's very versatile and beginner-friendly.
If you've used MySQL before and have the time and want to use all features of Knex.js and Objection.js, then get started with PostgreSQL to get some additional relational database experience.