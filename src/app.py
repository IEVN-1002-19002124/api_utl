
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    grupo = "IEVN 1002"
    lista = ["IEVN 1001","IEVN 1002","IEVN 1003"]
    return render_template('index.html',grupo = grupo)

@app.route('/hola')
def hola():
    return "Saludo UTL"

@app.route('/user/<string:nombre>')
def user1(nombre):
    return 'Saludo {0}'.format(nombre)

@app.route('/numero/<int:n1>')
def numero(n1):
    return 'El número es: {}'.format(n1)

@app.route('/user/<int:id>/<string:nom>')
def user2(id,nom):
    return 'ID: {0} Nombre: {1}'.format(id,nom)

@app.route('/suma/<float:n1>/<float:n2>')
def method_name(n1,n2):
    return 'La suma es {}'.format(n1+n2)

@app.route('/default')
@app.route('/default/<string:dd>')
def default(dd = 'Penjamo'):
    return '<h1>El nombre es: {} </h1>'.format(dd)

@app.route('/alumnos')
def alumnos():
    return render_template('alumnos.html')

if __name__ == "__main__":
    app.run(debug=True)