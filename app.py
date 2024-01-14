from flask import Flask, render_template, redirect
from opd import *

app = Flask(__name__)

@app.route('/')
def home():
    return "SPAK 2024"

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/<opd>')
def spak(opd):
    if opd not in opdAccronym:
        return redirect('/')
    else:
        return render_template('spak.html', perangkat_daerah=opdFullName[opd])




if __name__ == '__main__':
    app.run(debug=True)