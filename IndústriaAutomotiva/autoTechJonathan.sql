create database autotechJonathan;
use autotechJonathan;

create table pecas(
	id_peca int primary key auto_increment,
    nome_peca longtext not null,
    peso_peca float not null default 0.0,
    lote_peca date not null default '2025-05-29'
);

alter table pecas add column setor_peca longtext not null;

SELECT * FROM pecas;