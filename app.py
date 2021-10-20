from logging import debug
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True) 