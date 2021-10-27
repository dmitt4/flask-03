from flask import Flask, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from config import Config
from project.forms import CalcForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = CalcForm()

    if form.validate_on_submit():
        x = form.x.data
        oper = form.oper.data
        y = form.y.data

        return redirect(url_for('calc', x=x, oper=oper, y = y))
    
    return render_template('index.html', form=form)


@app.route('/calc/<int:x>/<oper>/<int:y>/', methods = ['GET'])
def calc(x: int, oper, y: int):
    operations = {
        '+': lambda x, y: x + y,
        ':': lambda x, y: x / y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '**': lambda x, y: x ** y}     

    result_aquired = (oper in operations) and not (oper == ':' and y == 0 )
    result = None
    if result_aquired:
        result = operations[oper](x,y) 

    return render_template('calc.html',
                            result_aquired = result_aquired,
                            result = result
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True) 


