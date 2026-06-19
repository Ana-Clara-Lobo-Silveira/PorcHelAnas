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
from model.carrinho import adicionar_item
from model.carrinho import obter_carrinho
from database.conexao import conectar


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
    id_produto = request.form.get("id_produto")
    nome = request.form.get("nome")
    comentario = request.form.get("comentario")

    if "usuario_c" not in session:
        return redirect("/pagina_login")
    
    if nome and comentario and id_produto:
        inserir_comentario(nome, comentario, id_produto)
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


@app.route("/adicionar_carrinho/<int:id_produto>", methods=["POST"])
def adicionar_carrinho(id_produto):
    if "usuario_c" not in session:
        return redirect("/pagina_login")
    
    email = session["email"]
    quantidade = 1 
    
    # Passo 1: Descobrimos o código do carrinho usando o e-mail
    cod_carrinho = obter_carrinho(email)
    
    # Passo 2: Conectamos o carrinho com o produto e a quantidade
    adicionar_item(cod_carrinho, id_produto, quantidade)
    
    # Depois de salvar no banco, para onde você quer redirecionar o usuário?
    return redirect("/")



@app.route("/meu_carrinho", methods=["GET"])
def meu_carrinho():
    if "usuario_c" not in session:
        return jsonify([]) # Retorna uma lista vazia se não estiver logado
        
    email = session ["usuario_c"]["email"]
    cod_carrinho = obter_carrinho(email)
    
    conexao, cursor = conectar()
    
    # Executamos o SELECT com o INNER JOIN que planejamos
    query = """
        SELECT i.quantidade, p.nome_produto, p.preco, p.imagem_produto 
        FROM itens_carrinho i
        INNER JOIN produtos p ON i.id_produto = p.id_produto
        WHERE i.cod_carrinho = %s
    """
    cursor.execute(query, (cod_carrinho,))
    
    # Pegamos todos os itens do banco
    itens = cursor.fetchall() 
    conexao.close()
    
    # Transformamos os dados em JSON para o JavaScript conseguir ler
    return jsonify(itens)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)

