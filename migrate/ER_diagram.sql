CREATE DATABASE IF NOT exists financas;
USE financas;

CREATE TABLE IF NOT EXISTS tb_usuarios (
 login VARCHAR(15) PRIMARY KEY NOT NULL,
 senha VARCHAR(200)
);



CREATE TABLE IF NOT EXISTS tb_categorias  (
 id_categoria INT PRIMARY KEY auto_increment,
 nome VARCHAR(20),
 login VARCHAR(15) NOT NULL
);



CREATE TABLE IF NOT EXISTS tb_despesas (
 id_despesas INT PRIMARY KEY auto_increment,
 data DATE,
 hora TIME(4),
 valor FLOAT(4),
 descricao VARCHAR(50),
 login VARCHAR(15) NOT NULL,
 id_categoria INT NOT NULL
);




ALTER TABLE tb_despesas ADD CONSTRAINT FK_tb_despesas_0 FOREIGN KEY (login) REFERENCES tb_usuarios (login);
ALTER TABLE tb_despesas ADD CONSTRAINT FK_tb_despesas_1 FOREIGN KEY (id_categoria) REFERENCES tb_categorias (id_categoria);


