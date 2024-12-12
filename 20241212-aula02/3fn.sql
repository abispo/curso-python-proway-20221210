/*
 * Terceira Forma Normal (3FN)
 * 
 * Uma tabela está na 3FN, se:
 * -> Está na 2FN (nenhuma das regras da 2FN está sendo violada)
 * -> Todas as colunas não-chave da tabela dependem exclusivamente da chave primária, e não de outros campos não-chave.
 * Chamamos essa dependência de dependendência transitiva
 */

CREATE DATABASE IF NOT EXISTS modulo02_python_aula02;
USE modulo02_python_aula02;

-- Criação da tabela de itens
CREATE TABLE IF NOT EXISTS tb_itens(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	valor_unitario FLOAT NOT NULL
);
DESC tb_itens;

INSERT INTO tb_itens(nome, valor_unitario) VALUES
	("Estojo", 4.99),
	("Caixa de Giz de Cera", 9.99),
	("Mochila Infantil", 39.99),
	("Lapiseira", 4.99),
	("Borracha", 2.99);
SELECT * FROM tb_itens;

-- Criação da tabela de pedidos
CREATE TABLE IF NOT EXISTS tb_pedidos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	data_hora DATETIME NOT NULL,
	descricao VARCHAR(200) NULL
);
DESC tb_pedidos;

INSERT INTO tb_pedidos(data_hora, descricao) VALUES ("2024-10-09 11:45:38", "Primeiro pedido na loja");
INSERT INTO tb_pedidos(data_hora) VALUES ("2024-10-01 17:12:14");
INSERT INTO tb_pedidos(data_hora) VALUES ("2024-10-11 09:04:55");
SELECT * FROM tb_pedidos;

-- Criar tabelas de itens dos pedidos
CREATE TABLE tb_itens_pedido(
	item_id INT NOT NULL,
	pedido_id INT NOT NULL,
	quantidade INT NOT NULL,
	subtotal FLOAT NOT NULL,
	PRIMARY KEY(item_id, pedido_id),
	FOREIGN KEY(item_id) REFERENCES tb_itens(id),
	FOREIGN KEY(pedido_id) REFERENCES tb_pedidos(id)
);
DESC tb_itens_pedido ;

INSERT INTO tb_itens_pedido (item_id, pedido_id, quantidade, subtotal) VALUES
	(1, 1, 2, 9.98),
	(2, 1, 1, 9.99),
	(2, 2, 1, 9.99),
	(3, 3, 1, 39.99),
	(4, 3, 3, 8.97);
SELECT * FROM tb_itens_pedido tip ;

SELECT tp.id AS pedido_id, ti.nome, ti.valor_unitario, tip.quantidade, tip.subtotal
	FROM tb_itens ti 
	INNER JOIN tb_itens_pedido tip 
	ON ti.id = tip.item_id
	INNER JOIN tb_pedidos tp 
	ON tip.pedido_id = tp.id;

-- No caso acima, a tabela tb_itens_pedido está violando a 3FN, pois a coluna subtotal depende de outra coluna não-chave(quantidade) para definir o seu valor
-- Para resolver isso, vamos apagar a coluna subtotal e gerá-la em tempo de execução.

ALTER TABLE tb_itens_pedido DROP COLUMN subtotal;

SELECT tp.id AS pedido_id, ti.nome, ti.valor_unitario, tip.quantidade, FORMAT(ti.valor_unitario * tip.quantidade, 2) AS "Subtotal"
	FROM tb_itens ti 
	INNER JOIN tb_itens_pedido tip 
	ON ti.id = tip.item_id
	INNER JOIN tb_pedidos tp 
	ON tip.pedido_id = tp.id;