from flask import Flask, render_template

app = Flask(__name__)


perangkat_daerah = {
        "dispendukcapil" : "Dinas Kependudukan dan Pencatatan Sipil",
        "dpmptsp" : "Dinas Penanaman Modal dan Perizinan Terpadu Satu Pintu"
    }

@app.route('/')
def home():
    return "Hello, my world"

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/<opd>')
def spak(opd):
    return render_template('spak.html', perangkat_daerah=perangkat_daerah[opd], opd=opd)




if __name__ == '__main__':
    app.run(debug=True)