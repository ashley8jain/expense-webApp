import datetime
from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)
mysql = MySQL(app)

color = ["","#bbdefb","#f0f4c3","#ffccbc","#e1bee7","#c8e6c9"]

category = ["","Grocery","Entertainment","Vehicle","Food","miscellaneous"]

# data = [
#     {
#         'id':1,
#         'category':1,
#         'info':'big bazaar-grocery',
#         'amount':24.0,
#         'date_created':'2018-02-19'
#     },
#     {
#         'id':2,
#         'category':2,
#         'info':'Movie - Entertainment',
#         'amount':21.0,
#         'date_created':'2018-02-20'
#     },
#     {
#         'id':3,
#         'category':3,
#         'info':'Petrol - Vehicle',
#         'amount':15.0,
#         'date_created':'2018-02-18'
#     },
#     {
#         'id':4,
#         'category':4,
#         'info':'leela rest - Vehicle',
#         'amount':93.0,
#         'date_created':'2018-01-01'
#     },
#     {
#         'id':5,
#         'category':5,
#         'info':'stationery - miscellaneous',
#         'amount':61.0,
#         'date_created':'2018-01-05'
#     }
# ]
# id = 6;
#
# def getDatas():
#     if result > 0:
#         return data
#     else:
#         return []

def addData(info,category,amount):

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO expense(info, category, amount, date_created) VALUES(%s, %s, %s, %s)",(info, category, amount,datetime.datetime.now().date()))
    mysql.connection.commit()
    cur.close()
    # global id;
    # expense = {
    #     'id':id,
    #     'category':category,
    #     'info':info,
    #     'amount':amount,
    #     'date_created':datetime.datetime.now().date()
    # };
    # id+=1;
    #
    # data.append(expense);
    return;

def getData(id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM expense WHERE id=%s",[id])
    data = cur.fetchone()
    cur.close()
    return data;
    # for data_i in data:
    #     if(data_i['id']==id):
    #         return data_i
    #
    # return;

def deleteData(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM expense WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    # for data_i in data:
    #     if(data_i['id']==id):
    #         data.remove(data_i)
    #         # print(data)
    #         break
    return;

def changeData(id,info,category,amount):
    oldData = getData(id)
    cur = mysql.connection.cursor()
    cur.execute ("UPDATE expense SET info=%s, category=%s, amount=%s WHERE id=%s",(info, category, amount, id))
    mysql.connection.commit()
    cur.close()
    # expense = {
    #     'id':id,
    #     'category':category,
    #     'info':info,
    #     'amount':amount,
    #     'date_created':oldData['date_created']
    # }
    # deleteData(id)
    # data.append(expense);
    return;
