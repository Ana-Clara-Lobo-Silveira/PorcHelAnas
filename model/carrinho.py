from database.conexao import conectar

def obter_carrinho(email):
    conexao, cursor = conectar()
    
    # 1. Tentamos encontrar um carrinho já existente para esse e-mail
    cursor.execute("SELECT cod_carrinho FROM carrinho WHERE email = %s", (email,))
    resultado = cursor.fetchone()
    
    if resultado:
        # Se achou, o cod_carrinho está aqui dentro
        cod_carrinho = resultado['cod_carrinho']
    else:
        # 2. Se não achou, inserimos um novo registro na tabela carrinho
        cursor.execute("INSERT INTO carrinho (email) VALUES (%s)", (email,))
        conexao.commit()
        
        # Descobrimos o ID que o banco acabou de gerar no auto_increment
        cod_carrinho = cursor.lastrowid
        
    conexao.close()
    return cod_carrinho



def adicionar_item(cod_carrinho, id_produto, quantidade):
    conexao, cursor = conectar()
    
    # 1. Verifica se o produto já está no carrinho desse utilizador
    cursor.execute(
        "SELECT cod_item, quantidade FROM itens_carrinho WHERE id_produto = %s AND cod_carrinho = %s", 
        (id_produto, cod_carrinho)
    )
    item_existente = cursor.fetchone()
    
    if item_existente:
        # 2. Se já existe, calcula a nova quantidade e atualiza (UPDATE)
        nova_qtd = item_existente['quantidade'] + quantidade
        cursor.execute(
            "UPDATE itens_carrinho SET quantidade = %s WHERE cod_item = %s", 
            (nova_qtd, item_existente['cod_item'])
        )
    else:
        # 3. Se não existe, insere um novo registo (INSERT)
        cursor.execute(
            "INSERT INTO itens_carrinho (id_produto, quantidade, cod_carrinho) VALUES (%s, %s, %s)", 
            (id_produto, quantidade, cod_carrinho)
        )
        
    conexao.commit()
    conexao.close()