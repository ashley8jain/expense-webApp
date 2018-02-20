from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, StringField, validators, IntegerField
import data
app = Flask(__name__)

datas = data.getDatas();

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html',datas = datas)



#add Expense
@app.route('/add_expense', methods=['POST','GET'])
def add_expense():
    form = expenseForm(request.form)
    if request.method == 'POST' and form.validate():
        info = form.info.data
        category = form.category.data
        amount = form.amount.data
        data.addData(info, category, amount)
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
        category = request.form['category']
        amount = request.form['amount']
        data.changeData(id, info, category, amount)
        return redirect(url_for('home'))

    return render_template('add_expense.html', form=form, title='Edit')

class expenseForm(Form):
    info = StringField('Info', [validators.Length(min=1)])
    category = IntegerField('Categry')
    amount = IntegerField('Amount')





#delete Expense
@app.route('/delete_expense/<int:id>', methods=['POST'])
def delete_expense(id):
    data.deleteData(id);
    return redirect(url_for('home'))





if __name__ == '__main__':
    app.run(debug=True)
