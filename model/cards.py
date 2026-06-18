from database.conexao import conectar

def recupera_card():
    conexao, cursor = conectar ()

    cursor.execute(""" SELECT nome_produto, descricao_produto, preco, imagem_produto, id_produto
                   FROM produtos; """)
    
    produto=cursor.fetchall()
    conexao.close()
    return produto