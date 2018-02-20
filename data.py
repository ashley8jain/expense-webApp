import datetime

data = [
    {
        'id':1,
        'category':1,
        'info':'big bazaar-grocery',
        'amount':24,
        'date':''
    },
    {
        'id':2,
        'category':2,
        'info':'Movie - Entertainment',
        'amount':21,
        'date':''
    },
    {
        'id':3,
        'category':3,
        'info':'Petrol - Vehicle',
        'amount':15,
        'date':''
    },
    {
        'id':4,
        'category':4,
        'info':'leela rest - Vehicle',
        'amount':93,
        'date':''
    },
    {
        'id':5,
        'category':5,
        'info':'stationery - miscellaneous',
        'amount':61,
        'date':''
    }
]
id = 6;

def getDatas():
    return data;

def addData(info,category,amount):
    global id;
    expense = {
        'id':id,
        'category':category,
        'info':info,
        'amount':amount,
        'date':datetime.datetime.now().date()
    };
    id+=1;

    data.append(expense);
    return;

def getData(id):
    for data_i in data:
        if(data_i['id']==id):
            return data_i

    return;

def deleteData(id):
    for data_i in data:
        if(data_i['id']==id):
            data.remove(data_i)
            # print(data)
            break

    return;

def changeData(id,info,category,amount):
    deleteData(id)
    expense = {
        'id':id,
        'category':category,
        'info':info,
        'amount':amount,
        'date':datetime.datetime.now().date()
    }

    data.append(expense);
    return;
