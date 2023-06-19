# Python - Object-relational mapping

This project covers Object relational mapping using sqlalchemy. It also gives introduction toon MySQLdb.
## Learning objectives
This project has satisfy the objectives such as knowing what object relational mappers are, their advantages, MySQLdb, introduction to SQLAlchemy, mysqlclient/MySQLdb, introduction to flask SQLAlchemy, how to connect MYSQL databse from a python script, how to SELECT AND INSERT rows in MYSQL table from a python script, mapping of python class to a MySQL table

## Requirements

* Editor: The editor used was vi
* pycodestyle version 2.8.x
* MySQLdb version 2.0.x
* SQLAlchemy version 1.4.x
* Files were interpreted / compilled on Ubuntu 20.04 LTS using python3

## How to install MySQLdb module version 2.0.x
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```
## How to install SQLAlchemy module version 1.4.x
```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
## How to connect to MySQL server without ORM using the module MySQLdb
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
## How to connect to MySQL server with an ORM like SQLAlchemy
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
## Author
Olowosuyi Temitope
