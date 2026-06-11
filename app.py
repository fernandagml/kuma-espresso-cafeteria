from flask import Flask, render_template
from model.categorias import recuperar_categorias as rc
from model.produtos import recuperar_produtos as rp, recuperar_produtos_por_categoria, recuperar_produto

app = Flask(__name__)

@app.route("/")
def index():
    categorias = rc()
    return render_template("inicio.html", categorias = categorias)

@app.route("/produtos/<id_categoria>")
def pagina_produtos(id_categoria):
    produtos = recuperar_produtos_por_categoria(id_categoria)
    return render_template("produtos.html", produtos = produtos)

@app.route("/produto/<id_produto>")
def pagina_produto(id_produto):
    produto = recuperar_produto(id_produto)
    return render_template("produto_unico.html", produto = produto)


@app.route("/como_chegar")
def pagina_como_chegar():
    return render_template("como_chegar.html")


if __name__ == "__main__":
    app.run(debug=True)
