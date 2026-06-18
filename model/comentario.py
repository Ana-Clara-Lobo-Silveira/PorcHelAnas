from database.conexao import conectar

def obter_comentario():
    conexao, cursor = conectar()
    cursor.execute(
            """ SELECT comentario, nome_completo FROM comentarios WHERE comentario =%s """
    )
    comentarios = cursor.fetchall()
    cursor.close()
    conexao.close()
    return comentarios
        

def inserir_comentario(comentario, nome_completo):
    conexao, cursor = conectar()
    cursor.execute(
            """
            INSERT INTO comentario (comentario, nome_completo) values (%s,%s)""", [comentario, nome_completo]
    )
    conexao.commit()
    conexao.close()