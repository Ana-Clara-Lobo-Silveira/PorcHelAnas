from flask import Flask, render_template, request, redirect, session, flash, jsonify
from model.cadastro import cadastro
app = Flask(__name__)
@app.route("/")
def pagina_inicial():
    return render_template("pagina_inicial.html")

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
        
        return redirect("/")
    else:
        return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)