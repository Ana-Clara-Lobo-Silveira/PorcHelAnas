from database.conexao import Conexao
def recupera_produto():
    conexao,cursor = Conexao.conexao()
    
    cursor.execute(""" SELECT nome_produto, descricao_produto, preco, imagem_produto, id_categoria
                   FROM produtos WHERE id_produto = ;""")

    produto=cursor.fetchone()

    conexao.close()

    return produto
