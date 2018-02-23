from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, StringField, validators, IntegerField, SelectField, FloatField
from flask_mysqldb import MySQL
import data

app = Flask(__name__)

#config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'expense'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# datas = data.getDatas();




@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM expense")
    datas = cur.fetchall()
    cur.close()
    mapp = dict()
    for dataa in datas:
        timee = str(dataa['date_created'])[2:7]
        if timee in mapp:
            mapp[timee]+=dataa['amount']
        else:
            mapp[timee]=dataa['amount']

    legend = 'total $'
    labels = []
    values = []
    for key in sorted(mapp,reverse=True):
        labels.append(key)
        values.append(mapp[key])


    # labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nove", "Dec"]
    # values = [10, 9, 8, 7, 6, 4, 7, 8, 10, 9, 8, 7]
    return render_template('home.html',datas = datas,color = data.color,category = data.category, values=values, labels=labels, legend=legend)



#add Expense
@app.route('/add_expense', methods=['POST','GET'])
def add_expense():
    form = expenseForm(request.form)
    if request.method == 'POST' and form.validate():
        info = form.info.data
        category = form.category.data
        amount = form.amount.data
        data.addData(info, category, amount)
        flash('Expense added', 'success')
        return redirect(url_for('home'))

    return render_template('add_expense.html', form=form, title='Add')



#edit expense
@app.route('/edit_expense/<int:id>', methods=['POST','GET'])
def edit_expense(id):
    data_i = data.getData(id)
    form = expenseForm(request.form)
    form.info.data = data_i['info']
    form.category.data = data_i['category']
    form.amount.data = data_i['amount']
    if request.method == 'POST' and form.validate():
        info = request.form['info']
        category = int(request.form['category'])
        amount = request.form['amount']
        data.changeData(id, info, category, amount)
        flash('Expense updated', 'success')
        return redirect(url_for('home'))

    return render_template('add_expense.html', form=form, title='Edit')

class expenseForm(Form):
    info = StringField('Info', [validators.Length(min=1)])
    category = SelectField(
        'Category',
        coerce=int,
        choices=[(1, 'Grocery'), (2, 'Entertainment'), (3, 'Vehicle'),(4, 'Food'),(5, 'miscellaneous')]
    )
    amount = FloatField('Amount')





#delete Expense
@app.route('/delete_expense/<int:id>', methods=['POST'])
def delete_expense(id):
    data.deleteData(id)
    flash('Expense deleted', 'success')
    return redirect(url_for('home'))





if __name__ == '__main__':
    app.secret_key='123abc'
    app.run(debug=True)
