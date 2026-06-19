from database.conexao import conectar

def recupera_cat_xic():
    conexao, cursor = conectar ()

    cursor.execute(""" SELECT nome_produto, descricao_produto, preco, imagem_produto, id_produto
                   FROM produtos where id_categoria = 1; """)
    
    xicaras=cursor.fetchall()
    conexao.close()
    return xicaras

def recupera_cat_bule():
    conexao, cursor = conectar ()

    cursor.execute(""" SELECT nome_produto, descricao_produto, preco, imagem_produto, id_produto
                   FROM produtos where id_categoria = 2; """)
    
    bules=cursor.fetchall()
    conexao.close()
    return bules

def recupera_cat_dec():
    conexao, cursor = conectar ()

    cursor.execute(""" SELECT nome_produto, descricao_produto, preco, imagem_produto, id_produto
                   FROM produtos where id_categoria = 3; """)
    
    decoracoes=cursor.fetchall()
    conexao.close()
    return decoracoes

def recupera_cat_prato():
    conexao, cursor = conectar ()

    cursor.execute(""" SELECT nome_produto, descricao_produto, preco, imagem_produto, id_produto
                   FROM produtos where id_categoria = 4; """)
    
    pratos=cursor.fetchall()
    conexao.close()
    return pratos

def recupera_cat_conj():
    conexao, cursor = conectar ()

    cursor.execute(""" SELECT nome_produto, descricao_produto, preco, imagem_produto, id_produto
                   FROM produtos where id_categoria = 5; """)
    
    conjuntos=cursor.fetchall()
    conexao.close()
    return conjuntos