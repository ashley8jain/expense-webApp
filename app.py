from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, StringField, validators
import data
app = Flask(__name__)

datas = data.getData();

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html',datas = datas)

# add Expense
@app.route('/add_expense', methods=['POST','GET'])
def add_expense():
    form = add_expenseForm(request.form)
    if request.method == 'POST' and form.validate():
        info = form.info.data
        category = form.category.data
        amount = form.amount.data
        data.addData(info, category, amount)
        return redirect(url_for('home'))

    return render_template('add_expense.html', form=form)

class add_expenseForm(Form):
    info = StringField('Info', [validators.Length(min=1)])
    category = StringField('Categry', [validators.Length(min=1)])
    amount = StringField('Amount', [validators.Length(min=1)])

if __name__ == '__main__':
    app.run(debug=True)
