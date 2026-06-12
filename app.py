from flask import Flask, render_template, request, redirect, session, flash, jsonify
from model.pagina_produto import recupera_produto

app = Flask(__name__)
@app.route("/")
def pagina_inicial():
    return render_template("pagina_inicial.html")

@app.route("/pagina_produto")
def pagina_produto():
    produto = recupera_produto()
    comentarios = []
    return render_template("pagina_produto.html", produto = produto, comentarios = comentarios)


@app.route("/pagina_cadastro")
def pagina_cadastro():
    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)