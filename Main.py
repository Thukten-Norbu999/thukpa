from flask import Flask,render_template
from Asia.sM import sM

app = Flask(__name__)
app.register_blueprint(sM,url_prefix="")

@app.route('/')
def choose():
    return render_template('base.html')



if __name__ == '__main__':
    app.run(debug=True)