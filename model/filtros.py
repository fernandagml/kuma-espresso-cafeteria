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
    
def recuperar_filtros_por_categoria(id_categoria, preco = None, subcategoria = None):
    """Função criada para buscar os filtros por produtos no banco de dados."""

    try:
        conexao, cursor = conectar()
        busca = []
        busca_base = """SELECT DISTINCT tb_filtros_produtos.id_filtro, tb_filtros_produtos.id_produto, tb_produtos.id_categoria, tb_filtros.nome_filtro, tb_produtos.preco_produto
                        FROM tb_filtros_produtos
                        INNER JOIN tb_filtros ON tb_filtros_produtos.id_filtro = tb_filtros.id_filtro
                        INNER JOIN tb_produtos ON tb_produtos.id_produto = tb_filtros_produtos.id_produto
                        WHERE id_categoria = %s"""
        busca.append(id_categoria)
        if preco:
            valor = preco.split('-')
            valor_min = float(valor[0])
            valor_max = float(valor[1])
            busca_base += " AND preco_produto BETWEEN %s AND %s"
            busca.append(valor_min)
            busca.append(valor_max)
        if subcategoria:
            busca_base += " AND id_filtro = %s"
            busca.append(subcategoria)
        cursor.execute(busca_base,busca)
        filtros_por_categoria = cursor.fetchall()
        conexao.close()
        return filtros_por_categoria
    
    except Exception as erro:
        print(erro)
        return False