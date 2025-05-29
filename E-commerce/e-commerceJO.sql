create database ecommerce;
use ecommerce;

create table produtos(
	id_prod int primary key auto_increment,
    nome_prod longtext not null,
    preco_prod float not null,
    estoque_prod int not null,
    avaliacao_prod float not null,
    categoria_prod longtext not null
);
 
 select * from produtos;