CREATE DATABASE IF NOT EXISTS db_kumaespresso;
USE db_kumaespresso;

CREATE TABLE IF NOT EXISTS tb_usuarios (
	nome_usuario VARCHAR(50) NOT NULL,
    usuario VARCHAR(50) PRIMARY KEY,
    email_usuario VARCHAR(100),
    telefone_usuario VARCHAR(12),
    endereco_usuario VARCHAR(100),
    senha_usuario VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS tb_categorias_produtos (
	id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    categoria VARCHAR(50),
    imagem_categoria VARCHAR(250)
);

CREATE TABLE IF NOT EXISTS tb_produtos (
	id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto VARCHAR(50) NOT NULL,
    preco_produto REAL NOT NULL,
    descricao_produto VARCHAR(500),
    descricao_detalhada VARCHAR(800),
    imagem_produto varchar(250),
    id_categoria INT,
    CONSTRAINT FK_produto_categoria
    FOREIGN KEY (id_categoria) REFERENCES tb_categorias_produtos(id_categoria)
);

CREATE TABLE IF NOT EXISTS tb_filtros (
	id_filtro INT PRIMARY KEY AUTO_INCREMENT,
    nome_filtro VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_filtros_produtos (
	id_produto INT,
    id_filtro INT,
    PRIMARY KEY(id_produto, id_filtro),
    CONSTRAINT FK_produto
    FOREIGN KEY (id_produto) REFERENCES tb_produtos(id_produto),
    CONSTRAINT FK_filtro 
    FOREIGN KEY (id_filtro) REFERENCES tb_filtros(id_filtro)
);

CREATE TABLE IF NOT EXISTS tb_comentarios (
	id_comentario INT AUTO_INCREMENT PRIMARY KEY,
    comentario VARCHAR(200),
    usuario VARCHAR(50),
    avaliacao INT,
    id_produto INT,
	CONSTRAINT FK_comentario_usuario
    FOREIGN KEY (usuario) REFERENCES tb_usuarios(usuario),
	CONSTRAINT FK_comentario_produto
    FOREIGN KEY (id_produto) REFERENCES tb_produtos(id_produto)
);