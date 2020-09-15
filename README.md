# Answer To StackOverFlow question

Link: https://stackoverflow.com/questions/63906296/how-to-use-db-execute-in-flask-sqlalchemy-inside-blueprint-without-any-models

## Replace placeholders

1. In app folder, `__init__.py` file,  
   replace `user`, `password`, `host` (localhost?), and `database_name`  
   in the `database_uri` variable

2. In app folder, `api` blueprint, `some_service` file,  
   replace `table-name` in the raw sql query.

## Run Flask

In the terminal (with an active virtual environment and dependencies)

```
pipenv shell
pipenv install
flask run
```

Then call,

```
http://127.0.0.1:5000/test
```

It should print results fetched from the db in the terminal.
