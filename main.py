from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

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
def mult():
        if request.method=="POST":
            num1= request.form.get("n1")
            num2= request.form.get("n2")
            return "<h1>El resultado es: {}</h1>".format(str(int(num1)*int(num2)))
        else:
            return  """ 
                        <form action="/multiplica" method="POST">
                            <label for="n1">N1:</label>
                            <input type="text" name="n1">
                            <label for="n2">N2:</label>
                            <input type="text" name="n2">
                            <input type="submit">
                        </form>
                    """
        
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