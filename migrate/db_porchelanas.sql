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
 descricao_produto VARCHAR(500),
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

-- ------------------ INSERTS ------
insert into categoria (nome_categoria) values ('xicaras');
insert into categoria (nome_categoria) values ('bules');
insert into categoria (nome_categoria) values ('decoracao');
insert into categoria (nome_categoria) values ('pratos');
insert into categoria (nome_categoria) values ('conjuntos');
select * from categoria;
select * from produtos;
INSERT INTO produtos (id_categoria, imagem_produto, nome_produto, descricao_produto, preco) VALUES 
(1, '1.jpg', 'Xícara Realeza Dourada com Toque Floral', 'Sofisticada xícara de porcelana branca fina, adornada com um imponente arabesco em ouro fosco e delicados ramos florais rosados. Perfeita para colecionadores e momentos especiais.', 145.00),

(1, '2.jpg', 'Xícara Botânica Hortênsia Azul', 'Uma peça romântica que evoca a tranquilidade dos jardins europeus. Apresenta uma pintura centralizada de flores em tons de azul e lilás, finalizada com uma elegante asa trabalhada em filete de ouro.', 138.00),

(1, '3.jpg', 'Xícara de Chá Rosas de Versalhes', 'Com um design clássico de perfil baixo e boca larga, esta xícara traz uma delicada guirlanda de rosas cor-de-rosa e acabamento dourado na borda ondulada. O charme do estilo shabby chic.', 150.00),

(2, '4.jpg', 'Bule Imperial de Porcelana Jardim de Inverno', 'A peça central que falta na sua mesa posta. Este magnífico bule de porcelana combina um formato clássico com uma rica estampa em tons de verde e amarelo claro, complementado por detalhes dourados na tampa e na asa.', 389.00),

(1, '5.jpg', 'Xícara de Porcelana Fina Bouquet Rosé', 'Elegância em cada detalhe. Xícara com silhueta agora e base elevada, destacando-se pela pintura rica de botões de rosa e uma asa dourada de design curvilíneo exclusivo.', 160.00),

(1, '6.jpg', 'Xícara Vintage Flores do Campo e Lavanda', 'Uma verdadeira obra de arte em porcelana. Esta peça apresenta um buquê detalhado de flores silvestres com destaque para tons de lavanda e rosa, sob uma borda ricamente trabalhada em filigrana dourada.', 155.00),

(1, '7.jpg', 'Xícara de Chá Clássica Azul Cobalto e Arabescos', 'Inspirada nos padrões de azulejaria e porcelana tradicional, esta xícara traz duas faixas distintas de estampas em azul sobre o fundo branco puro, criando um contraste sóbrio e atemporal.', 130.00),

(1, '8.jpg', 'Xícara Delicatezza Floral Magenta', 'Com uma proposta sutil e graciosa, esta xícara exibe ramos de flores em tom magenta e rosa antigo que parecem flutuar sobre a porcelana. A asa dourada reluzente coroa a peça.', 142.00),

(1, '9.jpg', 'Xícara de Chá Outono Dourado (Cítrica)', 'Trazendo calor e vivacidade para a mesa, esta xícara é decorada com delicadas ilustrações que remetem a pequenos frutos ou flores em tons de amarelo e laranja, emolduradas por uma generosa borda dourada.', 148.00),

(1, '10.jpg', 'Xícara de Chá Primavera Verdejante', 'Uma peça leve e fresca, decorada com ramas finas e pequenas flores silvestres em tons de verde-oliva e toques pastel. A borda superior interna e externa conta com um trabalhado texturizado impecável.', 135.00),
(1, '11.jpg', 'Xícara de Chá Romantismo Rosé', 'Delicada xícara de porcelana com estampa de rosas clássicas em tons suaves de rosa e contorno dourado na borda ondulada, perfeita para uma mesa posta elegante.', 145.00),

(1, '12.jpg', 'Xícara de Chá Realeza Verde Imperial', 'Com um refinado tom verde-oliva na borda texturizada e ramos florais delicados na base, esta peça une a sobriedade com o romantismo clássico.', 150.00),

(1, '13.jpg', 'Xícara de Chá Esplendor Dourado e Arabescos', 'Xícara de porcelana fina caracterizada por um imponente padrão de arabescos dourados em relevo e pequenos buquês de flores silvestres.', 160.00),

(1, '15.jpg', 'Xícara de Chá Jardim Secreto e Lavanda', 'Uma linda xícara com arranjos florais detalhados em tons de lavanda e magenta, finalizada com uma graciosa asa ornamentada em ouro.', 155.00),

(1, '16.jpg', 'Xícara de Chá Vintage Hortênsia e Ouro', 'Pintura marcante de flores azuis e roxas que contrastam perfeitamente com a alça dourada de design curvilíneo exclusivo.', 140.00),

(2, '17.jpg', 'Bule de Chá Clássica Azul Cobalto', 'Design atemporal com faixas ornamentais em azul cobalto, ideal para os amantes da porcelana tradicional de estilo europeu.', 335.00),

(2, '18.jpg', 'Bule de Chá Bouquet de Flores do Campo', 'Apresenta uma pintura suave de ramos florais e acabamento em ouro fosco na borda, trazendo leveza para a hora do chá.', 438.00),

(2, '19.jpg', 'Bule de Chá Outono Cítrico', 'Decorada com uma faixa de delicados frutos ou flores amarelas e alaranjadas, emoldurada por frisos dourados brilhantes.', 442.00),

(2, '20.jpg', 'Bule de Porcelana Imperial Jardim de Inverno', 'O ponto central da sua coleção. Este elegante bule traz uma rica estampa em tons de verde e amarelo claro, com acabamentos dourados impecáveis na tampa e na asa.', 389.00),
(2, '21.jpg', 'Bule de Porcelana Clássico Flores do Campo', 'Bule elegante com estampa botânica em tons de verde e dourado, perfeito para servir chá com sofisticação.', 389.00),
(2, '22.jpg', 'Bule de Porcelana Realeza Dourada', 'Design imponente com arabescos dourados e detalhes em amarelo pastel, ideal para mesas postas luxuosas.', 395.00),
(2, '23.jpg', 'Bule de Porcelana Outono Cítrico', 'Com ilustrações calorosas de flores e frutos em tons de amarelo e laranja, finalizado com ricos frisos em ouro.', 385.00),
(2, '24.jpg', 'Bule de Porcelana Toile de Jouy Preto', 'Estampa clássica estilo Toile de Jouy em preto e branco, trazendo um ar vintage e dramático para o serviço de chá.', 370.00),

(4, '25.jpg', 'Prato Raso Toile de Jouy Preto e Ouro', 'Prato de porcelana fina com borda ondulada decorada em padrões florais pretos clássicos e um delicado filete de ouro na aba.', 120.00),

(4, '26.jpg', 'Prato de Sopa / Fundo Imperial Arabescos Escuros', 'Prato fundo com centro Alvo e abas ricamente decoradas com arabescos e ramagens escuras, finalizado com acabamento em ouro fosco.', 135.00),

(4, '27.jpg', 'Prato de Sobremesa Azul de Delft Ondulado', 'Linda peça com bordas sinuosas e estampa floral geométrica em azul cobalto tradicional, inspirada na porcelana europeia.', 110.00),

(4, '28.jpg', 'Prato Raso Monograma Botânico Azul', 'Apresenta uma belíssima e delicada ilustração botânica centralizada em azul-pálido, emoldurada por uma aba trabalhada no mesmo tom.', 125.00),

(4, '29.jpg', 'Prato Raso Romantismo Rosé', 'Delicado prato com aba em tom rosa-chá texturizado e centro decorado com uma suave guirlanda de rosas clássicas.', 118.00),

(4, '30.jpg', 'Prato de Sobremesa Floral Rosa Antigo', 'Pintura minimalista com uma única flor geométrica ao centro e bordas decoradas com ramagens salpicadas em rosa antigo e ouro.', 115.00),
(4, '31.jpg', 'Prato de Chá Imperial Arabesco Amarelo', 'Prato com borda ondulada ricamente ornamentada em arabescos amarelos e dourados, ideal para composições ensolaradas de mesa posta.', 45.00),

(4, '32.jpg', 'Prato de Sobremesa Outono Dourado', 'Delicado prato com aba decorada em folhagens texturizadas douradas e fundo branco puro, trazendo calor e elegância atemporal.', 115.00),

(4, '33.jpg', 'Prato Fundo / Floreira de Mesa Botânica Verde', 'Peça versátil com borda festonada, decorada com delicadas ramagens verdes e pinceladas em tons pastéis e filete de ouro.', 138.00),


(5, '34.jpg', 'Conjunto de Chá Romântico Bouquet Rosé', 'Lindo jogo composto por bule e xícaras de porcelana fina com estampa clássica de rosas e elegantes asas banhadas a ouro.', 450.00),

(5, '35.jpg', 'Conjunto de Chá Minimalista Off-White', 'Conjunto moderno e clean em porcelana texturizada off-white, com design orgânico e acabamento fosco acetinado.', 390.00),

(5, '36.jpg', 'Conjunto de Chá Menta Vintage Flores do Campo', 'Sofisticado jogo de chá em tom verde-menta pastel com pintura interna floral e bule coordenado de silhueta clássica.', 480.00),

(5, '37.jpg', 'Conjunto de Mesa Monocromático Amarelo Sol', 'Conjunto vibrante composto por bules, xícaras e bowls em porcelana amarela brilhante de linhas limpas e contemporâneas.', 420.00),

(3, '38.jpg', 'Anfora de Porcelana Fina Flores Silvestres', 'Vaso estilo ânfora com duas alças ornamentadas em ouro, decorado com ricas pinturas táteis de flores do campo em tons quentes.', 290.00),

(3, '39.jpg', 'Vaso de Porcelana Clássico Azul de Delft', 'Vaso de formato balaustre com belíssima estampa botânica monocromática em azul cobalto, perfeito para decorações tradicionais.', 320.00),
(3, '40.jpg', 'Coleção Estatuetas Infantis Tons de Azul - Querubins Vintage', 'Conjunto delicado de estatuetas de porcelana pintadas à mão, retratando crianças com trajes clássicos em azul-pastel. Ricas em detalhes expressivos e acabamento acetinado.', 320.00),

(3, '41.jpg', 'Estatuetas Clássicas Blandford em Cristaleira', 'Lindo grupo de bonecas antigas de porcelana biscuit ao lado de miniaturas utilitárias florais. Perfeitas para colecionadores e decoração de ambientes românticos.', 280.00),

(3, '42.jpg', 'Conjunto Esculturas Animais da Floresta - Cervo e Filhotes', 'Gracioso grupo decorativo trazendo um cervo com acabamento esmaltado texturizado e pequenos filhotes de traços suaves em porcelana branca fina.', 240.00),

(3, '43.jpg', 'Par de Coelhos em Porcelana Branca Clássica', 'Duas elegantes estatuetas de coelhos em porcelana branca pura com alto brilho, acompanhadas ao fundo por cervos e louças decorativas em atmosfera de bosque.', 195.00);
