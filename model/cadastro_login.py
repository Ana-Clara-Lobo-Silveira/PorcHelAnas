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
    
def login (email, senha) -> list:
        con, cur  = conectar()
        cur.execute("SELECT nome_completo, email, senha FROM cadastro WHERE  email = %s AND senha=%s", [email, senha])
        login_executado = cur.fetchone()
        con.close()

        return login_executado
