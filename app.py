from flask import Flask, render_template, redirect, request, session, jsonify
from model.categorias import recuperar_categorias as rc
from model.produtos import recuperar_produtos as rp, recuperar_produtos_por_categoria, recuperar_produto
from model.usuarios import cadastrar, logar
from model.filtros import recuperar_filtros, recuperar_filtros_por_categoria
from model.comentarios import salvar_comentario, recuperar_comentarios

app = Flask(__name__)
app.secret_key = "cafeteria_kuma_espresso_chave"

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
    comentarios = recuperar_comentarios(id_produto)
    return render_template("produto_unico.html", produto = produto, comentarios = comentarios)


@app.route("/como_chegar")
def pagina_como_chegar():
    return render_template("como_chegar.html")

@app.route("/cadastro")
def cadastrando():
    return render_template("cadastro.html")


@app.route("/cadastro/post", methods=["POST"])
def cadastro_usuario():
    nome = request.form.get("nome")
    email_user = request.form.get("email")
    tel = request.form.get("tel")
    end = request.form.get("endereco")
    senha = request.form.get("senha")
    user = request.form.get("user")

    if cadastrar(nome, email_user, tel, end, senha, user):
        return render_template("login.html")
    else:
        return redirect("/")
    
@app.route("/login")
def autenticar():
    return render_template("login.html")

@app.route("/login/post", methods=["POST"])
def logar_usuario():
    user = request.form.get("user")
    senha = request.form.get("senha")

    usuario= logar(user, senha)

    if usuario:
        session["usuario_logado"] = usuario
        return redirect("/")
    else:
        return redirect("/cadastro")
    
@app.route("/logout")
def sair():
    session.clear()
    return redirect("/")


@app.context_processor
def carregar_categorias_menu():
    return {
        "categorias_menu": rc()
    }

@app.route("/comentario/post/<id_produto>", methods=["POST"])
def comentar(id_produto):
    comentario = request.form.get("comentario")
    if "usuario_logado" in session:
        usuario = session["usuario_logado"]["usuario"]
    avaliacao = request.form.get("star")
    salvar_comentario(comentario, usuario, avaliacao, id_produto)
    return redirect(f"/produto/{id_produto}")

if __name__ == "__main__":
    app.run(debug=True)
