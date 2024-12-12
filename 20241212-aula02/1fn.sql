/*
 * Primeira Forma Normal (1FN)
 * 
 * A Primeira Forma Normal define que cada coluna de uma tabela deve atender às seguintes regras:
 *  -> Deve existir ao menos 1 coluna que seja chave primária
 *  -> Pode conter apenas valores atômicos (ou indivisíveis)
 *  -> Não podem existir colunas multivaloradas
 */

CREATE DATABASE IF NOT EXISTS modulo02_python_aula02;
USE modulo02_python_aula02;

-- Criação da tabela tb_clientes
CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT NOT NULL,
	nome VARCHAR(100),
	endereco VARCHAR(200),
	telefone VARCHAR(50)
);
DESC tb_clientes ;

INSERT INTO tb_clientes (id, nome, endereco, telefone) VALUES
	(1, "João da Silva", "Rua XV de Novembro, 1000, Centro, Blumenau, SC", "47999998888"),
	(2, "Neide Carvalho", "Praça da Liberdade, 12, Liberdade, São Paulo, SP", "47911111111,47911112222"),
	(3, "Maria Souza", "Rua dos Bandeirantes, 240, Centro, Pomerode, SC", "47944444444");
SELECT * FROM tb_clientes ;
SELECT * FROM tb_clientes WHERE endereco LIKE "%SP%";

/*
A tabela acima viola a 1FN, pois:
	-> Não existe chave primária na tabela
	-> A coluna endereço é uma coluna composta. Ou seja, podemos dividir esse valor para outras colunas
	-> A coluna telefone possui registros multivalorados
*/
RENAME TABLE tb_clientes TO tb_clientes_pre_1fn;

CREATE TABLE IF NOT EXISTS tb_clientes (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	tipo_logradouro VARCHAR(20) NOT NULL,
	logradouro VARCHAR(100) NOT NULL,
	numero VARCHAR(10) NOT NULL,
	bairro VARCHAR(50) NOT NULL,
	cidade VARCHAR(50) NOT NULL,
	uf CHAR(2) NOT NULL
);
DESC tb_clientes;

INSERT INTO tb_clientes (id, nome, tipo_logradouro, logradouro, numero, bairro, cidade, uf) VALUES
	(1, "João da Silva", "Rua", "XV de Novembro", "1000", "Centro", "Blumenau", "SC"),
	(2, "Neide Carvalho", "Praça", "da Liberdade", "12", "Liberdade", "São Paulo", "SP"),
	(3, "Maria Souza", "Rua", "dos Bandeirantes", "240", "Centro", "Pomerode", "SC");
SELECT * FROM tb_clientes;

-- Acima resolvemos 2 problemas: Definimos a chave primária da tabela e "quebramos" a coluna endereço em várias outras colunas
-- No caso da coluna telefone, como pode possuir registros multivalorados, a saída é criar uma tabela para armazenar os telefones dos clientes

CREATE TABLE IF NOT EXISTS tb_telefones(
	id INT PRIMARY KEY AUTO_INCREMENT,
	cliente_id INT NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	FOREIGN KEY(cliente_id) REFERENCES tb_clientes(id)
);
DESC tb_telefones ;

INSERT INTO tb_telefones (cliente_id, telefone) VALUES
	(1, "47999998888"),
	(2, "47911111111"),
	(2, "47911112222"),
	(3, "47944444444");
SELECT * FROM tb_telefones ;

-- Trazer os clientes e os seus telefones
SELECT tc.id, tc.nome, tt.telefone
	FROM tb_clientes tc 
	INNER JOIN tb_telefones tt 
	ON tc.id = tt.cliente_id ;

-- Com isso, aplicamos todas as regras da 1FN na tabela tb_clientes
