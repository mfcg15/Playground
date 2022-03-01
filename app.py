from turtle import color
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", funcion="", veces=0)

@app.route('/play')
def play():
    return render_template("index.html",funcion="play",veces=3, color="#9fc4f8")

@app.route('/play/<int:rango>')
def playX(rango):
    return render_template("index.html",funcion="playX", veces=rango, color="#9fc4f8")

@app.route('/play/<int:rango>/<string:bc>')
def playColor(rango,bc):
    return render_template("index.html",funcion="playX", veces=rango, color=bc)

if __name__=="__main__":
    app.run(debug=True)