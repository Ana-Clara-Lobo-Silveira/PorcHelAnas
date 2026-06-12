CREATE DATABASE porchelanas;
USE porchelanas;

CREATE TABLE cadastro (
 email VARCHAR(100) NOT NULL PRIMARY KEY,
 nome_completo VARCHAR(150),
 telefone VARCHAR(15),
 endereco VARCHAR(200),
 senha VARCHAR(8)
);




CREATE TABLE IF NOT EXISTS carrinho (
 cod_carrinho INT auto_increment NOT NULL primary key,
 email VARCHAR(100)
);



CREATE TABLE IF NOT EXISTS categoria (
 id_categoria INT auto_increment NOT NULL PRIMARY KEY,
 nome_categoria VARCHAR(50)
);



CREATE TABLE IF NOT EXISTS produtos (
 id_produto INT auto_increment NOT NULL PRIMARY KEY,
 nome_produto VARCHAR(100),
 descricao_produto VARCHAR(200),
 preco FLOAT,
 imagem_produto VARCHAR(255),
 id_categoria INT
);



CREATE TABLE IF NOT EXISTS comentarios (
 cod_comentario INT auto_increment NOT NULL PRIMARY KEY,
 id_produto INT,
 comentario VARCHAR(300),
 nome_completo VARCHAR(50)
);



CREATE TABLE IF NOT EXISTS itens_carrinho (
 cod_item INT auto_increment NOT NULL PRIMARY KEY,
 id_produto INT,
 quantidade INT,
 cod_carrinho INT
);



ALTER TABLE carrinho ADD CONSTRAINT FK_carrinho_0 FOREIGN KEY (email) REFERENCES cadastro (email);


ALTER TABLE produtos ADD CONSTRAINT FK_produtos_0 FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria);


ALTER TABLE comentarios ADD CONSTRAINT FK_comentarios_0 FOREIGN KEY (id_produto) REFERENCES produtos (id_produto);


ALTER TABLE itens_carrinho ADD CONSTRAINT FK_itens_carrinho_0 FOREIGN KEY (id_produto) REFERENCES produtos (id_produto);
ALTER TABLE itens_carrinho ADD CONSTRAINT FK_itens_carrinho_1 FOREIGN KEY (cod_carrinho) REFERENCES carrinho (cod_carrinho);


