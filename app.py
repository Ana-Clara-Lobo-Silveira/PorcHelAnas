from flask import Flask, render_template, request, redirect, session, flash, jsonify, url_for
from model.cadastro_login import cadastro
from model.cadastro_login import login
from model.cards import recupera_card
from model.pagina_produto import recupera_produto
from model.categorias import recupera_cat_xic
from model.categorias import recupera_cat_bule
from model.categorias import recupera_cat_dec
from model.categorias import recupera_cat_prato
from model.categorias import recupera_cat_conj
from model.pagina_produto import obter_comentarios
from model.pagina_produto import inserir_comentario

app = Flask(__name__)
app.secret_key = "PorcHelAnas"

# PÁGINA PRINCIPAL------------------------------
@app.route("/")
def pagina_inicial():
    cards = recupera_card()
    return render_template("pagina_inicial.html",produto = cards)

# CATEGORIAS------------------------------------
@app.route("/xicaras")
def pagina_inicial_x():
    r_xicaras = recupera_cat_xic()
    return render_template("pagina_inicial.html",produto = r_xicaras)

@app.route("/bules")
def pagina_inicial_b():
    r_bules = recupera_cat_bule()
    return render_template("pagina_inicial.html",produto = r_bules)

@app.route("/decoracao")
def pagina_inicial_d():
    r_decoracao = recupera_cat_dec()
    return render_template("pagina_inicial.html",produto = r_decoracao)

@app.route("/pratos")
def pagina_inicial_p():
    r_pratos = recupera_cat_prato()
    return render_template("pagina_inicial.html",produto = r_pratos)

@app.route("/conjuntos")
def pagina_inicial_c():
    r_conjuntos = recupera_cat_conj()
    return render_template("pagina_inicial.html",produto = r_conjuntos)

# PÁGINA PRODUTO----------------------------
@app.route("/pagina_produto/<id_produto>")
def pagina_produto(id_produto):
    produtos_u = recupera_produto(id_produto)
    coment = obter_comentarios(id_produto)
    return render_template("pagina_produto.html", produto = produtos_u, comentarios = coment, id_produto=id_produto)

@app.route("/e_comentario", methods=["POST"])
def enviar_comentario():
    if "usuario_c" not in session:
        return redirect("/pagina_login")  


    id_produto = request.form.get("id_produto")
    comentario = request.form.get("comentario")
    nome_completo = session['usuario_c']['nome_completo']


    
    if comentario and id_produto:
        inserir_comentario(nome_completo, comentario, id_produto)
    return redirect(url_for("pagina_produto", id_produto=id_produto))


# PÁGINA CADASTRO---------------------------
@app.route("/pagina_cadastro", methods = ["GET"])
def pagina_cadastro():
    return render_template("cadastro.html")


@app.route("/pagina_cadastro", methods = ["POST"])
def pg_cadastro():
    nome_completo = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    endereco = request.form.get("endereco")
    senha = request.form.get("senha")
    if cadastro(nome_completo, email, telefone, endereco, senha):
        
        return redirect("/pagina_login")
    else:
        return render_template("cadastro.html")

# PÁGINA LOGIN LOGOUT----------------------------
@app.route("/pagina_login", methods = ["GET"])
def pg_login_get():
    return render_template("login.html")

@app.route("/pagina_login", methods = ["POST"])
def pg_login():
    email = request.form.get("email")
    senha = request.form.get("senha")

    usuario_conectado= login(email,senha)

    if usuario_conectado:
        session["usuario_c"] = usuario_conectado
        return redirect("/")
    else:
        return redirect("/pagina_login")
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)

