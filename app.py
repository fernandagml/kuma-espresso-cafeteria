from flask import Flask, render_template, redirect, request
from model.categorias import recuperar_categorias as rc
from model.produtos import recuperar_produtos as rp, recuperar_produtos_por_categoria, recuperar_produto
from model.usuarios import cadastrar, logar
from model.filtros import recuperar_filtros, recuperar_filtros_por_categoria

app = Flask(__name__)

@app.route("/")
def index():
    categorias = rc()
    return render_template("inicio.html", categorias = categorias)

@app.route("/produtos/<id_categoria>")
def pagina_produtos(id_categoria):
    produtos = recuperar_produtos_por_categoria(id_categoria)
    filtros = recuperar_filtros()
    filtros_por_categoria = recuperar_filtros_por_categoria(id_categoria)
    return render_template("produtos.html", produtos = produtos, filtros = filtros, filtros_por_categoria = filtros_por_categoria)

@app.route("/produto/<id_produto>")
def pagina_produto(id_produto):
    produto = recuperar_produto(id_produto)
    return render_template("produto_unico.html", produto = produto)


@app.route("/cadastro")
def cadastrando():
    return render_template("cadastro.html")


@app.route("/cadastro/post", methods=["POST"])
def cadastro_usuario():
    email_user = request.form.get("email_usuario")
    senha = request.form.get("senha_usuario")

    if cadastrar(email_user, senha):
        return render_template("login.html")
    else:
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)