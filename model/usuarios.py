from database.conexao import conectar

def cadastrar (nome_usuario, email, telefone, endereco, senha):
    try:
        conexao, cursor = conectar()
        cursor.execute("INSERT INTO tb_usuarios (nome_usuario, email_usuario, telefone_usuario, endereco_usuario, senha_usuario) VALUES (%s, %s, %s, %s, %s);", [nome_usuario, email, telefone, endereco, senha])
        conexao.commit()
        conexao.close()
    except Exception as erro:
        print(erro)
        return False
    

def logar(email:str, senha:str) -> dict:
    try:
        conexao, cursor = conectar()
        cursor.execute("SELECT email_usuario, nome_usuario from tb_usuarios WHERE email_usuario = %s and senha_usuario = %s;", [email, senha])
        resultado = cursor.fetchone()
        conexao.close()
        return resultado
    
    except Exception as erro:
        print(erro)
        return False
