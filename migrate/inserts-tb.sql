INSERT INTO tb_categorias_produtos (categoria, imagem_categoria)
VALUES ("Cafés", "../static/img/cafes-categoria_semfundo.png"),
		("Doces", "../static/img/doces-semfundo.png"),
        ("Chás", "../static/img/chas-semfundo.png"),
        ("Bebidas Doces", "../static/img/bebidas-semfundo.png");
        
INSERT INTO tb_produtos (nome_produto, preco_produto, descricao_produto, imagem_produto, id_categoria)
VALUES ("Café Preto", 8.90, "descricao", "../static/img/cafe-preto.jpg", 1),
		("Café Descafeinado", 8.90, "descricao", "../static/img/cafe-descafeinado.jpg", 1),
        ("Café com Leite", 8.90, "descricao", "../static/img/cafe-com-leite.jpg", 1),
		("Chá Gelado", 8.90, "descricao", "../static/img/cha-gelado.jpg", 3),
        ("Milkshake Blueberry", 8.90, "descricao", "../static/img/milkshake-blueberry.jpg", 4),
        ("Milkshake Caramelo", 8.90, "descricao", "../static/img/milkshake-caramelo.jpg", 4),
        ("Milkshake de Chocolate com Nozes", 8.90, "descricao", "../static/img/milkshake-chocolateComNozes.jpg", 4),
        ("Milkshake Meio Amargo", 8.90, "descricao", "../static/img/milkshake-meioAmargo.jpg", 4),
        ("Milkshake de Morango", 8.90, "descricao", "../static/img/milkshake-morango.jpg", 4),
        ("Milkshake de Oreo", 8.90, "descricao", "../static/img/milkshake-oreo.jpg", 4);
        
INSERT INTO tb_filtros (nome_filtro)
VALUES ("Sem açucar"), ("Sem lactose"), ("Gelado"), ("Com leite"), ("Milkshake");