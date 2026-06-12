INSERT INTO tb_categorias_produtos (categoria, imagem_categoria)
VALUES ("Cafés", "../static/img/cafes-categoria_semfundo.png"),
		("Doces", "../static/img/doces-semfundo.png"),
        ("Chás", "../static/img/chas-semfundo.png"),
        ("Bebidas Doces", "../static/img/bebidas-semfundo.png");
        
INSERT INTO tb_produtos (nome_produto, preco_produto, descricao_produto, imagem_produto, id_categoria)
VALUES ("Café Preto", 8.90, "descricao", "../static/img/cafe-preto.jpg", 1),
		("Café Descafeinado", 8.90, "descricao", "../static/img/cafe-descafeinado.jpg", 1),
        ("Café com Leite", 8.90, "descricao", "../static/img/cafe-com-leite.jpg", 1),
        ("Milkshake Blueberry", 8.90, "descricao", "../static/img/milkshake-blueberry.jpg", 4),
        ("Milkshake Caramelo", 8.90, "descricao", "../static/img/milkshake-caramelo.jpg", 4),
        ("Milkshake de Chocolate com Nozes", 8.90, "descricao", "../static/img/milkshake-chocolateComNozes.jpg", 4),
        ("Milkshake Meio Amargo", 8.90, "descricao", "../static/img/milkshake-meioAmargo.jpg", 4),
        ("Milkshake de Morango", 8.90, "descricao", "../static/img/milkshake-morango.jpg", 4),
        ("Milkshake de Oreo", 8.90, "descricao", "../static/img/milkshake-oreo.jpg", 4),
        ("Brownie", 8.90, "descricao", "../static/img/brownie.jpg", 2),
        ("Cookies", 8.90, "descricao", "../static/img/cookies.jpg", 2),
        ("Torta de Morango", 8.90, "descricao", "../static/img/torta-morango.jpg", 2),
        ("Bomboms da casa", 8.90, "descricao", "../static/img/bomboms-da-casa.jpg", 2),
        ("Biscoff", 8.90, "descricao", "../static/img/biscoff.jpg", 2),
        ("Petit Gateau", 8.90, "descricao", "../static/img/petit-gateau.jpg", 2),
        ("Banofe", 8.90, "descricao", "../static/img/banofe.jpg", 2),
        ("Red Velvet", 8.90, "descricao", "../static/img/red-velvet.jpg", 2),
        ("Bolo de Chocolate", 8.90, "descricao", "../static/img/bolo-chocolate.jpg", 2),
        ("Chá de Limão", 8.90, "descricao", "../static/img/cha-limao.jpg", 3),
        ("Chá de Hibisco", 8.90, "descricao", "../static/img/cha-hibisco.jpg", 3),
        ("Chá Gelado de Limão", 8.90, "descricao", "../static/img/cha-gelado.jpg", 3),
        ("Chá verde", 8.90, "descricao", "../static/img/cha-verde.jpg", 3),
        ("Chá Gelado de Pêssego", 8.90, "descricao", "../static/img/cha-gelado-pessego.jpg", 3),
        ("Chá de Camomila", 8.90, "descricao", "../static/img/cha-camomila.jpg", 3),
        ("Chá de Hortelã", 8.90, "descricao", "../static/img/cha-hortela.jpg", 3),
        ("Chá Gelado de Frutas Vermelhas", 8.90, "descricao", "../static/img/cha-gelado-fv.jpg", 3),
        ("Chá Oolong", 8.90, "descricao", "../static/img/cha-oolong.jpg", 3);
        
        
INSERT INTO tb_filtros (nome_filtro)
VALUES ("Sem açucar"), ("Sem lactose"), ("Gelado"), ("Com leite"), ("Milkshake");

INSERT INTO tb_filtros_produtos (id_produto, id_filtro)
VALUES (3, 4);