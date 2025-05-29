import mysql.connector
import time as t

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'clinicaJo'
)

cursor = conexao.cursor()
print("Conexão bem-sucedida!")

def menu():
    print("\nBem-vindo à Clínica Médica!")
    print("1. Cadastrar Paciente")
    print("2. Listar Paciente")
    print("3. Atualizar Paciente")
    print("4. Excluir Paciente")
    print("5. Sair")
    
escolha = 0

while escolha != 5:
    menu()
    escolha = int(input("Escolha uma opção: "))
    
    match escolha:
        case 1:
            print("\n--- Cadastro de Paciente ---")
            nome = input("Digite o nome do paciente: ")
            idade = int(input("Digite a idade do paciente: "))
            tipo_sanguineo = input("Digite o tipo sanguíneo do paciente: ")
            ultima_consulta = input("Digite a data da última consulta do paciente: ")

            comando = f"INSERT INTO pacientes (nome_paciente, idade_paciente, tipoSanguineo_paciente, ultima_consulta_paciente) VALUES ('{nome}', {idade}, '{tipo_sanguineo}', '{ultima_consulta}')"
            cursor.execute(comando)
            conexao.commit()
            print("Paciente cadastrado com sucesso!")
            t.sleep(1)
            
        case 2:
            print("\n--- Lista de Pacientes com Consulta nos Útlimos 30 Dias ---")
            comando = "SELECT * FROM pacientes where ultima_consulta_paciente > '2025-04-29' ORDER BY ultima_consulta_paciente DESC"
            cursor.execute(comando)
            pacientes = cursor.fetchall()
            t.sleep(1)
            
            if pacientes:
                for paciente in pacientes:
                    print(f"\nID: {paciente[0]}\nNome: {paciente[1]}\nIdade: {paciente[2]}\nTipo Sanguíneo: {paciente[3]}\nÚltima Consulta: {paciente[4]}")
                    t.sleep(1)
            else:
                print("\nNenhum paciente cadastrado.")
                t.sleep(1)
                
        case 3:
            print("\n--- Atualização de Paciente ---")
            id = int(input("Digite o ID do paciente a ser atualizado: "))
            comando = f"SELECT * FROM pacientes where id_pacientes = {id}"
            cursor.execute(comando)
            pacientes = cursor.fetchall()
            t.sleep(1)
            
            if pacientes:
                ultima_consulta = input("Digite a nova data da última consulta do paciente: ")
                comando = f"UPDATE pacientes SET ultima_consulta_paciente ='{ultima_consulta}' WHERE id_pacientes = {id}"
                cursor.execute(comando)
                conexao.commit()
                print("Paciente atualizado com sucesso!")
                t.sleep(1)
            else:
                print("\nNenhum paciente cadastrado.")
                t.sleep(1)
    
        case 4:
            print("\n--- Exclusão de Pacientes cujo Última consulta faz mais de 2 anos ---")
            comando = f"DELETE FROM pacientes WHERE ultima_consulta_paciente < '2023-05-29'"
            cursor.execute(comando)
            conexao.commit()
            print("\n       ---- Pacientes excluído com sucesso! ----")
            t.sleep(1)
            
        case 5:
            print("\nSaindo do sistema...")
            t.sleep(1)
            cursor.close()
            conexao.close()
