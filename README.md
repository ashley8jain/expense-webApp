# Expense webapp

> Step to run the webapp

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

* run the create_db.sql file to create table and insert datas in mysql server

* run the flask app
```
$ python app.py
```
* open the link [localhost:5000](localhost:5000)

> Docs

### Feature
* Responsive site
* search, category, date, period statement filter
* API endpoint (edit expense,add expense,delete expense) with POST methods
* Data Storage in MySql dababase
* Graph Visualization using chart.js API
