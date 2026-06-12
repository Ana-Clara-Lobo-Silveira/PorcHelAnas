from flask import Flask, render_template, request, redirect, session, flash, jsonify

app = Flask(__name__)
@app.route("/")
def pagina_inicial():
    return render_template("pagina_inicial.html")

@app.route("/pagina_produto")
def pagina_produto():
    return render_template("pagina_produto.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)