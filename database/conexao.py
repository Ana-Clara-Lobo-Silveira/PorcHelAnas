import mysql.connector


def conexao():
    conexao = mysql.connector.connect(
            host="localhost",
            port = 3306,
            user = "root",
            password="root",
            database = "porchelanas"
    )
    cursor = conexao.cursor(dictionary=True)

    return conexao, cursor