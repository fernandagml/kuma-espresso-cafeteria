from database.conexao import conectar

def recuperar_filtros():
    """Função criada para buscar os filtros dos produtos no banco de dados."""

    try:
        conexao, cursor = conectar()
        cursor.execute("SELECT id_filtro, nome_filtro FROM tb_filtros;")
        filtros = cursor.fetchall()
        conexao.close()
        return filtros
    
    except Exception as erro:
        print(erro)
        return False
    
def recuperar_filtros_por_categoria(id):
    """Função criada para buscar os filtros por produtos no banco de dados."""

    try:
        conexao, cursor = conectar()
        cursor.execute("SELECT tb_filtros_produtos.id_filtro, tb_filtros_produtos.id_produto, tb_produtos.id_categoria, tb_filtros.nome_filtro FROM tb_filtros_produtos INNER JOIN tb_filtros ON tb_filtros_produtos.id_filtro = tb_filtros.id_filtro INNER JOIN tb_produtos ON tb_produtos.id_produto = tb_filtros_produtos.id_produto WHERE id_categoria = %s;", (id, ))
        filtros_por_categoria = cursor.fetchall()
        conexao.close()
        return filtros_por_categoria
    
    except Exception as erro:
        print(erro)
        return False