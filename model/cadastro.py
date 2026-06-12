from database.conexao import conectar

def cadastro (nome_completo, email, telefone, endereco, senha):
    try:
        conexao, cursor  = conectar()
        cursor.execute("INSERT INTO cadastro (nome_completo, email, telefone, endereco, senha) VALUES (%s, %s, %s, %s, %s)", [nome_completo,email, telefone, endereco, senha])
        conexao.commit()
        conexao.close()

        return True
    except Exception as erro:
        print(erro)
        return False