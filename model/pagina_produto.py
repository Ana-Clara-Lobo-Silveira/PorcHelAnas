from database.conexao import conectar

def recupera_produto():
    conexao,cursor = conectar()
    
    cursor.execute(""" SELECT nome_produto, descricao_produto, preco, imagem_produto, id_categoria
                   FROM produtos WHERE id_produto = ;""")

    produto=cursor.fetchone()

    conexao.close()

    return produto
