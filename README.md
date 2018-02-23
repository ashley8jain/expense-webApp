# Expense webapp
[Live web-app](http://ashley8jain.pythonanywhere.com/)

Developed the web-app using flask framework with MySQL database and deploy to [pythonanywhere.com](https://www.pythonanywhere.com/)

> Step to run the webapp

* clone the github repo

* run the terminal command
```
$ cd expense-webApp
$ source bin/activate
$ pip install -r requirements.txt
```

* install MySQL software

* configure the mysql property in [app.py](/app.py) (MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)

* run the (create_db.sql)[/create_db.sql] file to create table and insert datas in mysql server

* run the flask app
```
$ python app.py
```
* open the link localhost:5000

> Docs

### Feature
* Responsive site
* search, category, date, period statement filter
* API endpoint (edit expense,add expense,delete expense) with POST methods
* Data Storage in MySql dababase
* Graph Visualization using chart.js API

### Docs
> Filter
* set Start and End Date for period statement
* change category
* search any word(info,category,date,amount) from expense list table

> Database Storage

* **Table**: expense(id int auto_increment,info text,category int NOT NULL,amount float,date_created date,primary key(id))
* Select,update,delete SQL statement in [data.py](/data.py)

> Restful API

* add new expense
```
POST method
request url: localhost:5000/add_expense
key: info (string), category (int), amount (float)
```

* edit expense
```
POST method
request url: localhost:5000/edit_expense/<id>
key: info (string), category (int), amount (float)
```

* delete expense
```
POST method
request url: localhost:5000/delete_expense/<id>
```
