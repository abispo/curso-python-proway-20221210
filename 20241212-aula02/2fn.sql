/*
 * Segunda Forma Normal (2FN)
 * 
 * A tabela está na 2FN, quando:
 * -> Ela está na 1FN
 * -> Não existem dependências parciais, ou seja, todas as colunas não-chave da tabela dependem totalmente de todas as partes da chave primária.
 * Chamamos isso de dependência funcional total
 */

CREATE DATABASE IF NOT EXISTS modulo02_python_aula02;
USE modulo02_python_aula02;

-- Criação da tabela de cursos
CREATE TABLE IF NOT EXISTS tb_cursos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	carga_horaria INT NOT NULL
);
DESC tb_cursos ;

INSERT INTO tb_cursos(nome, carga_horaria) VALUES
	("Fundamentos de Python", 20),
	("Java Avançado", 40),
	("Criação de APIs com Golang", 40);
SELECT * FROM tb_cursos tc ;

-- Criação da tabela de instrutores de cursos
CREATE TABLE IF NOT EXISTS tb_cursos_instrutores(
	curso_id INT NOT NULL,
	instrutor_id INT NOT NULL,
	nome_instrutor VARCHAR(100) NOT NULL,
	email_instrutor VARCHAR(100) NOT NULL,
	PRIMARY KEY(curso_id, instrutor_id),
	FOREIGN KEY(curso_id) REFERENCES tb_cursos(id)
);
DESC tb_cursos_instrutores ;

-- Inseridos dados que relacionam cursos com instrutores
INSERT INTO tb_cursos_instrutores (curso_id, instrutor_id, nome_instrutor, email_instrutor) VALUES
	(1, 1, "João da Silva", "joao.silva@email.com"),
	(2, 2, "Paulo Carvalho", "paulo.carvalho@email.com"),
	(3, 3, "Maria Rocha", "maria.rocha@email.com");
SELECT * FROM tb_cursos_instrutores;

INSERT INTO tb_cursos (nome, carga_horaria) VALUES
	("Introdução a Machine Learning com Python", 30);
	
INSERT INTO tb_cursos_instrutores (curso_id, instrutor_id, nome_instrutor, email_instrutor) VALUES
	(4, 3, "Maria Silva", "armando.genaro@email.com");
	
/*
 * No caso acima, temos um problema com relação so instrutor de id 3. Temos informações divergentes em linhas diferentes, por exemplo, o mesmo instrutor_id com
 * emails diferentes. Nesse caso, isso aconteceu pois as colunas nome_instrutor e email_instrutor dependem apenas de parte da chave primária, o que pode levar
 * a inconsistências nos registros
 * Para resolver isso, vamos criar uma tabela de instrutores e segregar as informações de nome e email nessa tabela.
 */

RENAME TABLE tb_cursos_instrutores TO tb_cursos_instrutores_pre_2fn;

-- 1º Passo: Criar a tabela de instrutores
CREATE TABLE IF NOT EXISTS tb_instrutores(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL
);
DESC tb_instrutores;
INSERT INTO tb_instrutores (nome, email) VALUES
	("João da Silva", "joao.silva@email.com"),
	("Paulo Carvalho", "paulo.carvalho@email.com"),
	("Maria Rocha", "maria.rocha@email.com");
SELECT * FROM tb_instrutores ti ;

-- 2º Passo: Criar a nova tabela de cursos_instrutores
ALTER TABLE tb_cursos_instrutores_pre_2fn DROP FOREIGN KEY tb_cursos_instrutores_pre_2fn_ibfk_1;
CREATE TABLE IF NOT EXISTS tb_cursos_instrutores(
	curso_id INT NOT NULL,
	instrutor_id INT NOT NULL,
	PRIMARY KEY(curso_id, instrutor_id),
	FOREIGN KEY(curso_id) REFERENCES tb_cursos(id),
	FOREIGN KEY(instrutor_id) REFERENCES tb_instrutores(id)
);
DESC tb_cursos_instrutores;

INSERT INTO tb_cursos_instrutores (curso_id, instrutor_id) VALUES
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 3);
SELECT * FROM tb_cursos_instrutores tci ;

-- Mostrar os instrutores e os cursos a que estão atribuídos
SELECT ti.id, ti.nome, ti.email, tc.nome, tc.carga_horaria
	FROM tb_instrutores ti 
	INNER JOIN tb_cursos_instrutores tci 
	ON ti.id = tci.instrutor_id 
	INNER JOIN tb_cursos tc 
	ON tc.id = tci.curso_id ;
