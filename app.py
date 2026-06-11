from flask import Flask, render_template
from model.categorias import recuperar_categorias as rc

app = Flask(__name__)

@app.route("/")
def index():
    categorias = rc()
    return render_template("inicio.html", categorias = categorias)

if __name__ == "__main__":
    app.run(debug=True)