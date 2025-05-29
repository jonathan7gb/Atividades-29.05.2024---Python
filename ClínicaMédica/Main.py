import mysql.connector
import time as t


conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'escolaJo'
)

cursor = conexao.cursor()
print("Conexão bem-sucedida!")