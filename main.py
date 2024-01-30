from flask import Flask, request, render_template
import forms
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    alum_form=forms.UserForm(request.form)
    if request.method=='POST':
        nom=alum_form.nombre.data
        apaterno=alum_form.apaterno.data
        email=alum_form.email.data
        print('Nombre: {}'.format(nom))
        print('Apaterno: {}'.format(apaterno))
        print('Correo: {}'.format(email))
    return render_template("alumnos.html", form=alum_form, nom=nom)

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/")
def hola():
    return "<p> Hola mundo </p>"

@app.route("/hola")
def func():
    return "<h1>Saludo desde Hola -UTL Bien!!-</h1>"

@app.route("/saludo")
def func1():
    return "<h1>Hola desde saludo</h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "<h1>Hola</h1>"+nom

@app.route("/numero/<int:n1>")
def numero(n1):
    return "<h1>El numero es: {}</h1>".format(n1)

@app.route("/user/<string:nom>/<int:id>")
def user(nom,id):
    return "<h1>ID: {}, Nombre: {}</h1>".format(id,nom)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "<h1>La suma de  {}  + {}  es: {}</h1>".format(n1,n2, n1+n2)

@app.route("/multiplica", methods=["GET", "POST"])
def operasBas():
    
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        op=request.form.get("op")

        if op=="sum":
            return "<h2> La suma es: {}</h2>".format(str(int(num1)+int(num2)))
        if op=="rest":
            return "<h2> La resta es: {}</h2>".format(str(int(num1)-int(num2)))
        if op=="mult":
            return "<h2> La multiplicacio es: {}</h2>".format(str(int(num1)*int(num2)))

        if op=="div":
            return "<h2> La division es: {}</h2>".format(str(int(num1)/int(num2)))    


        return "<h2>No ingresaste los numeros</h2>".format(str(int(num1)+int(num2)))

    else:
       return '''
        <form action="/operasBas" method="POST">
        <label> N1: </label>
        <input type="text" name="num1"/></br></br>
        <label> N2: </label>
        <input type="text" name="num2"/></br></br>
        
        
        <input type="radio" id="suma" name="op" value="sum">
        <label for="suma">Suma</label>

        <input type="radio" id="resta" name="op" value="rest">
        <label for="resta">Resta</label><br>
        
        <input type="radio" id="multi" name="op" value="mul">
        <label for="multi">Multiplicacion</label><br>
       
        <input type="radio" id="div" name="op" value="div" >
        <label for="div">Division</label><br>
        
        <input type="submit" value="calcular"/><br></br></br>

        </form>
        '''
        
@app.route("/formulario1")
def calculo():
    return render_template("formulario1.html")

@app.route("/resultado", methods=["GET", "POST"])
def mult2():
        if request.method=="POST":
            num1= request.form.get("n1")
            num2= request.form.get("n2")
            return "<h1>El resultado es: {}</h1>".format(str(int(num1)*int(num2)))
        else:
             pass

if __name__ == "__main__":
    app.run(debug=True)