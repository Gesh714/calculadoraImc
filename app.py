from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key="colocolo300394"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        peso = float(request.form["peso"])
        talla = float(request.form["talla"])

        imc = round(peso / (talla ** 2),2)
        descripcion = ""

        if imc < 18.5:
            descripcion = "Bajo peso"
        elif 18.5 <= imc < 24.9:
            descripcion = "Peso normal"
        elif 25 <= imc < 29.9:
            descripcion = "Sobrepeso" 
        else:
            descripcion = "Obesidad"

        return render_template("index.html", imc=imc, descripcion=descripcion)

    return render_template("index.html", imc="", descripcion="")

if __name__ == "__main__":
    app.run()
