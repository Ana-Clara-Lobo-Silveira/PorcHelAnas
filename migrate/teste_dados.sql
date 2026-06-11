-- Cadastro de usuários
INSERT INTO cadastro (email, nome_completo, telefone, endereco, senha)
VALUES
('joao@email.com', 'João Silva', '(16) 99705-8404', 'Rua A, São Paulo', '123456'),
('maria@email.com', 'Maria Oliveira', '(16) 99705-8404', 'Rua B, São Paulo', 'abcdef'),
('carlos@email.com', 'Carlos Souza', '(16) 99705-8404', 'Rua C, São Paulo', 'senha123');


INSERT INTO categoria (nome_categoria)
VALUES
('Pratos'),
('Xícaras'),
('Vasos'),
('Decoração');

INSERT INTO produtos (nome_produto, descricao_produto, preco, imagem_produto, id_categoria)
VALUES
('Prato de Porcelana Branco', 'Prato elegante de porcelana branca', 49.90, 'prato_branco.jpg', 1),
('Xícara Floral', 'Xícara com estampa floral', 29.90, 'xicara_floral.jpg', 2),
('Vaso Decorativo Azul', 'Vaso moderno azul em porcelana', 89.90, 'vaso_azul.jpg', 3),
('Enfeite de Mesa', 'Peça decorativa para mesa', 59.90, 'enfeite_mesa.jpg', 4);

INSERT INTO comentarios (id_produto, comentario, nome_completo)
VALUES
(1, 'Produto muito bonito e resistente!', 'João Silva'),
(2, 'Amei a estampa da xícara.', 'Maria Oliveira'),
(3, 'Excelente acabamento.', 'Carlos Souza');

SELECT * FROM cadastro;
SELECT * FROM produtos;
SELECT * FROM itens_carrinho;