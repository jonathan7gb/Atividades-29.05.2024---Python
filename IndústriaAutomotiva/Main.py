import mysql.connector
import time as t

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'autotechJonathan'
)

cursor = conexao.cursor()
print("Conexão bem-sucedida!")

def menu():
    print("\nBem-vindo ao sistema de gestão de indústria automotiva!")
    print("1 - Cadastrar peça")
    print("2 - Buscar peças")
    print("3 - Editar peça")
    print("4 - Excluir peça")
    print("5 - Sair")

escolha = 0

while escolha != 5:
    menu()
    escolha = int(input("Escolha uma opção: "))
    
    match escolha:
        case 1:
            print("\n-- Cadastro de Peça --")
            nome = input("Digite o nome da peça: ")
            peso = float(input("Digite o peso da peça: "))
            lote = input("Digite a data do lote: (YYYY-MM-DD): ")
            setor = input("Digite o setor da peça: ")
            
            comando = f"INSERT INTO pecas (nome_peca, peso_peca, lote_peca, setor_peca) VALUES ('{nome}', {peso}, '{lote}', '{setor}')"
            cursor.execute(comando)
            conexao.commit()
            print("\nPeça cadastrada com sucesso!")
        
        case 2:
            print("\n-- Busca de Peças --")
            print("1 - Buscar por ID")
            print("2 - Buscar por nome")
            print("3 - Buscar por lote (YYYY-MM-DD)")
            print("4 - Buscar por setor")
            escolha_busca = int(input("Escolha uma opção: "))
            
            if escolha_busca == 1:
                id = int(input("Digite o ID da peça a ser buscada: "))
                comando = f"SELECT * FROM pecas WHERE id_peca = {id}"
                cursor.execute(comando)
                resultados = cursor.fetchall()
                t.sleep(0.5)
                
                if resultados:
                    print("\nPeças encontradas:")
                    for resultado in resultados:
                        print(f"ID: {resultado[0]}\nNome: {resultado[1]}\nPeso: {resultado[2]} kg\nLote: {resultado[3]}\nSetor: {resultado[4]}")
                        t.sleep(0.5)
                else:
                    print("\n-- Nenhuma peça encontrada com esse ID --")
                    t.sleep(0.5)
                    
            elif escolha_busca == 2:
                nome = input("Digite o nome da peça a ser buscada: ")
                comando = f"SELECT * FROM pecas WHERE nome_peca LIKE '%{nome}%'"
                cursor.execute(comando)
                resultados = cursor.fetchall()
                t.sleep(0.5)
                
                if resultados:
                    print("\nPeças encontradas:")
                    for resultado in resultados:
                        print(f"ID: {resultado[0]}\nNome: {resultado[1]}\nPeso: {resultado[2]} kg\nLote: {resultado[3]}\nSetor: {resultado[4]}")
                        t.sleep(0.5)
                else:
                    print("\n-- Nenhuma peça encontrada com esse nome --")
                    t.sleep(0.5)
                    
            elif escolha_busca == 3:
                lote = input("Digite o lote da peça a ser buscada: ")
                comando = f"SELECT * FROM pecas WHERE lote_peca = '{lote}'"
                cursor.execute(comando)
                resultados = cursor.fetchall()
                t.sleep(0.5)
                
                if resultados:
                    print("\nPeças encontradas:")
                    for resultado in resultados:
                        print(f"ID: {resultado[0]}\nNome: {resultado[1]}\nPeso: {resultado[2]} kg\nLote: {resultado[3]}\nSetor: {resultado[4]}")
                        t.sleep(0.5)
                else:
                    print("\n-- Nenhuma peça encontrada nesse lote --")
                    t.sleep(0.5)
                    
            elif escolha_busca == 4:
                setor = input("Digite o setor da peça a ser buscada: ")
                comando = f"SELECT * FROM pecas WHERE setor_peca = '{setor}'"
                cursor.execute(comando)
                resultados = cursor.fetchall()
                t.sleep(0.5)
                
                if resultados:
                    print("\nPeças encontradas:")
                    for resultado in resultados:
                        print(f"ID: {resultado[0]}\nNome: {resultado[1]}\nPeso: {resultado[2]} kg\nLote: {resultado[3]}\nSetor: {resultado[4]}")
                        t.sleep(0.5)
                else:
                    print("\n-- Nenhuma peça encontrada nesse setor --")
                    t.sleep(0.5)
                    
            else:
                print("\n-- Opção inválida --")
                t.sleep(0.5)
                
        case 3:
            print("\n-- Edição de Peça --")
            id = int(input("Digite o ID da peça a ser editada: "))
            comando = f"SELECT * FROM pecas WHERE id_peca = '{id}'"
            cursor.execute(comando)
            resultados = cursor.fetchall()
            
            if resultados:
                peso = float(input("Digite o novo peso da peça: ")) 
                comando = f"UPDATE pecas SET peso_peca = {peso} WHERE id_peca = {id}"
                cursor.execute(comando)
                conexao.commit()
                print("\nPeça atualizada com sucesso!") 
            else:
                print("\n-- Nenhuma peça encontrada com esse ID --")
                
        case 4:
            print("\n-- Exclusão de Peça --")
            print("1 - Pelo ID")
            print("2 - Pelo lote")
            escolha_exclusao = int(input("Escolha uma opção: "))
            
            if escolha_exclusao == 1:
                id = int(input("Digite o ID da peça a ser excluída: "))
                comando = f"SELECT * FROM pecas WHERE id_peca = {id}"
                cursor.execute(comando)
                resultados = cursor.fetchall()
                t.sleep(0.5)
                
                if resultados:
                    comando = f"DELETE FROM pecas WHERE id_peca = {id}"
                    cursor.execute(comando)
                    conexao.commit()
                    print("\nPeça excluída com sucesso!")
                    t.sleep(0.5)
                else:
                    print("\n-- Nenhuma peça encontrada com esse ID --")
                    t.sleep(0.5)
            
            elif escolha_exclusao == 2:
                lote = input("Digite o lote da peça a ser excluída: ")
                comando = f"SELECT * FROM pecas WHERE lote_peca = '{lote}'"
                cursor.execute(comando)
                resultados = cursor.fetchall()
                t.sleep(0.5)
                
                if resultados:
                    comando = f"DELETE FROM pecas WHERE lote_peca = '{lote}'"
                    cursor.execute(comando)
                    conexao.commit()
                    print("\nPeça excluída com sucesso!")
                    t.sleep(0.5)
                else:
                    print("\n-- Nenhuma peça encontrada nesse lote --")
                    t.sleep(0.5)
                
            else:
                print("\n-- Opção inválida --")
                t.sleep(0.5)
        
        case 5:
            print("\nSaindo do sistema...")
            t.sleep(0.5)
            cursor.close()
            conexao.close()