from database.conexao import conectar

def salvar_comentario(comentario, usuario, avaliacao, id_produto):
    try:
        conexao, cursor = conectar()
        cursor.execute("INSERT INTO tb_comentarios (comentario, usuario, avaliacao, id_produto) VALUES (%s, %s, %s, %s);", (comentario, usuario, avaliacao, id_produto))
        conexao.commit()
        conexao.close()

    except Exception as erro:
        print(erro)
        return False
    
def recuperar_comentarios(id_produto):
    try:
        conexao, cursor = conectar()
        cursor.execute("SELECT * FROM tb_comentarios WHERE id_produto = %s;", (id_produto, ))
        comentarios = cursor.fetchall()
        conexao.close()
        return comentarios

    except Exception as erro:
        print(erro)
        return False
    


def excluir_comentario(id_comentario):
    try:
        conexao, cursor = conectar()
        cursor.execute("DELETE FROM tb_comentarios WHERE id_comentario = %s;", (id_comentario, ))
        conexao.commit()
        conexao.close()
        return True
    except Exception as erro:
        print(erro)
        return False