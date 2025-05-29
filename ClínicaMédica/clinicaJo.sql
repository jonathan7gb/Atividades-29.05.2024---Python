create database clinicaJo;
use clinicaJo;

create table pacientes(
	id_pacientes int primary key auto_increment,
    nome_paciente longtext not null,
    idade_paciente int not null,
    tipoSanguineo_paciente enum('o+', 'o-', 'a+', 'a-', 'b+', 'b-', 'ab+', 'ab-') not null,
    ultima_consulta_paciente date not null
);

select * from pacientes;
