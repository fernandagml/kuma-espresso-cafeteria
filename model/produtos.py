from database.conexao import conectar

def recuperar_produtos():
    """Função criada para buscar os produtos no banco de dados."""

    try:
        conexao, cursor = conectar()
        cursor.execute("SELECT id_produto, nome_produto, preco_produto, descricao_produto, imagem_produto, id_categoria FROM tb_produtos;")
        produtos = cursor.fetchall()
        conexao.close()
        return produtos
    
    except Exception as erro:
        print(erro)
        return False

def recuperar_produtos_por_categoria(id):
    """Função criada para buscar os produtos por categoria no banco de dados."""

    try:
        conexao, cursor = conectar()
        cursor.execute("SELECT tb_produtos.id_produto, tb_produtos.nome_produto, tb_produtos.preco_produto, tb_produtos.descricao_produto, tb_produtos.imagem_produto, tb_categorias_produtos.id_categoria, tb_categorias_produtos.categoria FROM tb_produtos INNER JOIN tb_categorias_produtos ON tb_produtos.id_categoria = tb_categorias_produtos.id_categoria WHERE tb_produtos.id_categoria = %s;", (id, ))
        produtos_por_categoria = cursor.fetchall()
        conexao.close()
        return produtos_por_categoria
    
    except Exception as erro:
        print(erro)
        return False
    
def recuperar_produto(id):
    """Função criada para buscar o produto individual no banco de dados."""

    try:
        conexao, cursor = conectar()
        cursor.execute("SELECT id_produto, nome_produto, preco_produto, descricao_produto, imagem_produto, id_categoria, descricao_detalhada FROM tb_produtos WHERE id_produto = %s;", (id, ))
        produto = cursor.fetchone()
        conexao.close()
        return produto
    
    except Exception as erro:
        print(erro)
        return False