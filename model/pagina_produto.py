from database.conexao import conectar

def pagina_produto():
    conexao,cursor = conectar()
    
    cursor.execute(""" SELECT nome_produto, descricao_produto, preco, imagem_produto, id_categoria
                   FROM produtos WHERE = %s""")

    produto=cursor.fetchone()

    conexao.close()

    return produto
