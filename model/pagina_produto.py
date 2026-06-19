from database.conexao import conectar

def recupera_produto(id_produto):
    conexao,cursor = conectar()
    
    cursor.execute(""" SELECT nome_produto, descricao_produto, preco, imagem_produto, id_categoria
                   FROM produtos WHERE id_produto = %s;""", [id_produto])

    produto=cursor.fetchone()

    conexao.close()

    return produto

def obter_comentarios(id_produto):
    conexao, cursor = conectar()
    cursor.execute(
            """
            select cod_comentario, nome_completo, id_produto, comentario from comentarios where id_produto = %s

            """, [id_produto]
    )
    comentarios = cursor.fetchall()
    cursor.close()
    conexao.close()
    return comentarios
        

def inserir_comentario(nome_completo, comentario, id_produto):
    conexao, cursor = conectar()
    cursor.execute(
            """
            insert into comentarios (nome_completo,comentario,id_produto) values (%s,%s,%s)""", [nome_completo, comentario, id_produto]
    )
    conexao.commit()
    conexao.close()