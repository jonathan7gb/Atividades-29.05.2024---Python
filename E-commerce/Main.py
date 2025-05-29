import mysql.connector
import time as t


conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'ecommerce'
)

cursor = conexao.cursor()
print("Conexão bem-sucedida!")

def menu():
    print("\nBem-vindo ao E-commerce MarketFast!")
    print("1. Cadastrar Produtos")
    print("2. Listar Produtos")
    print("3. Atualizar Produtos")
    print("4. Excluir Produtos")
    print("5. Listar por Categoria")
    print("6. Sair")
    
escolha = 0

while escolha != 6:
    menu()
    escolha = int(input("Escolha uma opção: "))
    
    match escolha:
        case 1:
            print("\n--- Cadastro de Produtos ---")
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            estoque = int(input("Digite a quantidade em estoque do produto: "))
            avaliacao = float(input("Digite a nota de avaliação do produto: "))
            categoria = input("Digite a categoria do produto: ")

            comando = f"INSERT INTO produtos (nome_prod, preco_prod, estoque_prod, avaliacao_prod, categoria_prod) VALUES ('{nome}', {preco}, {estoque}, {avaliacao}, '{categoria}')"
            cursor.execute(comando)
            conexao.commit()
            print("Produto cadastrado com sucesso!")
            t.sleep(1)
            
        case 2:
            print("\n--- Lista de Produtos com Avaliação > 4.0 ---")
            comando = "SELECT * FROM produtos where avaliacao_prod > 4.0 ORDER BY avaliacao_prod DESC"
            cursor.execute(comando)
            produtos = cursor.fetchall()
            t.sleep(1)
            
            if produtos:
                for produto in produtos:
                    print(f"\nID: {produto[0]}\nNome: {produto[1]}\nPreço: R${produto[2]:.2f}\nEstoque: {produto[3]}\nAvaliação: {produto[4]}\nCategoria: {produto[5]}")
                    t.sleep(1)
            else:
                print("\nNenhum produto cadastrado.")
                t.sleep(1)
                
        case 3:
            print("\n--- Atualização de Produto ---")
            id = int(input("Digite o ID do produto a ser atualizado: "))
            comando = f"SELECT * FROM produtos where id_prod = {id}"
            cursor.execute(comando)
            produto = cursor.fetchall()
            
            if produto:
                novo_preco = input("Digite o novo preço do produto (ou pressione Enter para manter o mesmo): ")
                novo_preco = float(novo_preco) if novo_preco else produto[2]
                novo_estoque = input("Digite a nova quantidade em estoque (ou pressione Enter para manter o mesmo): ")
                novo_estoque = int(novo_estoque) if novo_estoque else produto[3]

                comando_update = f"UPDATE produtos SET preco_prod = {novo_preco}, estoque_prod = {novo_estoque} WHERE id_prod = {id}"
                cursor.execute(comando_update)
                conexao.commit()
                print("Produto atualizado com sucesso!")
                t.sleep(1)
            else:
                print("\nProduto não encontrado.")
                t.sleep(1)
                
        case 4:
            print("\n--- Exclusão de Produtos sem Estoque ---")
            comando_delete = f"DELETE FROM produtos WHERE estoque_prod <= 0"
            cursor.execute(comando_delete)
            conexao.commit()
            print("\nProdutos excluídos com sucesso!")
            t.sleep(1)
            
        case 5:
            print("\n--- Listar Produtos por Categoria ---")
            categoria = input("Digite a categoria dos produtos: ")
            comando = f"SELECT * FROM produtos WHERE categoria_prod = '{categoria}'"
            cursor.execute(comando)
            produtos_categoria = cursor.fetchall()
            t.sleep(1)
            
            if produtos_categoria:
                for produto in produtos_categoria:
                    print(f"\nID: {produto[0]}\nNome: {produto[1]}\nPreço: R${produto[2]:.2f}\nEstoque: {produto[3]}\nAvaliação: {produto[4]}\nCategoria: {produto[5]}")
                    t.sleep(1)
            else:
                print("\nNenhum produto encontrado nessa categoria.")
                t.sleep(1)
                
        case 6:
            print("\nSaindo do sistema...")
            t.sleep(1)