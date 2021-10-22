from logging import debug
from os import abort
from flask import Flask, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from config import Config
from project.forms import MessageForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/calc', methods = ['POST'])
def calc():
    operations = {
        '+': lambda x, y: x + y,
        '/': lambda x, y: x / y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '**': lambda x, y: x ** y}     

    x = request.form.get('X', type=float)
    oper = request.form.get('oper', type=str)
    y = request.form.get('Y', type=float)

    result_aquired = (oper in operations) and not (oper == '/' and y == 0 )
    result = None
    if result_aquired:
        result = operations[oper](x,y) 

    return render_template('calc.html',
                            result_aquired = result_aquired,
                            result = result
    )

@app.route('/message/', methods=['get', 'post'])
def message():
    form = MessageForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(f'{name} {email} {message}')
        print('\nData recieved. Now redirecting...')
        return redirect(url_for('message'))
    
    return render_template('message.html', form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True) 


