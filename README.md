# Expense webapp

## Step to run the webapp

* clone the github repo

* run the terminal command
```
$ source bin/activate
```

* install all library

```
pip install -r requirements.txt
```

* install mysql package globally

* configure the mysql property in app.py (MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)

* run the create_db.sql file to create table in mysql server

* run the flask app
```
$ python app.py
```

## What have I done

* Install flask app

```
virtualenv expense-webApp
cd expense-webApp
source bin/activate
pip install flask
```

* create app.py file

* run the flask app

```
python app.py
```

* to create required library

```
pip freeze > requirements.txt
```
