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