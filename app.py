from flask import Flask, render_template, request, redirect, session, flash, jsonify

app = Flask(__name__)
@app.route("/")
def pagina_inicial():
    return render_template("pagina_inicial.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)