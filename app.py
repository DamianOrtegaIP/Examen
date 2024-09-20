from flask import Flask , render_template,request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def calcularTotal():
    if request.method == 'POST':
        nombre=str(request.form['nombre'])
        edad=int(request.form['edad'])
        tarros=int(request.form['tarros'])
        total_sinDesc= 9000*tarros
        if edad >= 18 and edad <= 30:
            desc= total_sinDesc * 0.15
            resultado= total_sinDesc - desc
        elif edad > 30:
            desc = total_sinDesc * 0.25
            resultado = total_sinDesc - desc
        else:
            desc = 0
            resultado = total_sinDesc
        return render_template('ejercicio1.html', desc=desc, resultado=resultado,total_sinDesc=total_sinDesc,nombre=nombre)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def verificarSesion():
    if request.method == 'POST':
        nombre=str(request.form['nombre'])
        contrasena=str(request.form['contrasena'])
        if nombre =='juan' and  contrasena == 'admin':
            resultado= 'Bienvenido adminstrador juan'
        elif nombre =='pepe' and  contrasena == 'user':
            resultado = 'Bienvenido usuario pepe'
        else:
            resultado = 'Usuario o contrasena incorrectas'
        return render_template('ejercicio2.html',resultado=resultado)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run()
