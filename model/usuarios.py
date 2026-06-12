from database.conexao import conectar

def cadastro (nome_usuario, email, ):
    try:
        conexao, cursor = conectar()
        cursor.execute("INSERT INTO usuario (nome_usuario, senha) VALUES (%s, %s);", [nome_usuario, senha] )
        conexao.commit()
        conexao.close()
    except Exception as erro:
        print(erro)
        return False