from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/input_data')
def input():
    return render_template('input_data.html')

@app.route('/list_data')
def list():
    return render_template('list_data.html')

if __name__ == '__main__':
    app.run('127.0.0.1',4000,debug=True)