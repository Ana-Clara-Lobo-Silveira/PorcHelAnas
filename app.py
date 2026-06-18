from flask import Flask, render_template, request, redirect, session, flash, jsonify
from model.cadastro_login import cadastro
from model.cadastro_login import login
from model.cards import recupera_card
app = Flask(__name__)
app.secret_key = "PorcHelAnas"


@app.route("/")
def pagina_inicial():
    cards = recupera_card()
    return render_template("pagina_inicial.html",produto = cards)

@app.route("/pagina_produto")
def pagina_produto():
    
    return render_template("pagina_produto.html")

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
    




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)

