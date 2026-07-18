import mysql.connector
import os
import time
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1310",
    database="farmacia")
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM produtos")
global dicionario_dados
dicionario_dados = cursor.fetchall()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def Inicio():
    limpar_tela()
    opcao = int(input("""
1 - Pesquisar Remédios
2 - Verificar Todos
3 - Comprar
4 - Adicionar Estoque ao Produto
5 - Remover Estoque do Produto
6 - Adicionar Produto
7 - Remover Produto
8 - Sair
Escolha: """))
    match opcao: 
      case 1:
        #pesquisar Remédio
        limpar_tela()
        Pesquisa()
      case 2:
        #Verificar Todos os Remédios
        limpar_tela()
        Verificar_Todos_Remedios()
      case 3:
        #Comprar  
        limpar_tela()
        Comprar()
      case 8:
        #Sair
        limpar_tela()
        conn.commit()
        print("Programa Finalizado")
        time.sleep(3)
        exit()
      case 4:
       #Adicionar Estoque ao Produto
       limpar_tela()
       add_estoque()
      case 5:
        #Remover Estoque ao Produto
        limpar_tela()
        Remover()
      case 6:
        #Adicionar Produto
        limpar_tela()
        adicionar_produto()
      case 7:
        limpar_tela()
        remover_produto()
      case _:
        #Caso Der Algum erro no input
        print("Erro")
        time.sleep(2)
        voltar_menu()
def Verificar_Todos_Remedios():
  #Verificar Todos os remedios
  print("Lista de Remédios:\n-------------------")
  i = 0 
  for remedio in dicionario_dados:
    print(f"{remedio["nome"]}: {remedio["quantidade"]}")
    print("-------------------")
    i += 1
  if i < 1:
    print("Nenhum Produto cadastrado")
  voltar_menu()
def Pesquisa():
  #Pesquisar Remedios
  nome_pesquisado = input("Digite o nome a ser pesquisado:\n ")
  for remedio in dicionario_dados:
    if nome_pesquisado.lower().strip() == remedio["nome"].lower().strip() and remedio["quantidade"] > 0:
      limpar_tela()
      print("Produto está em Estoque")
      print(f"Quantidade em estoque: {remedio['Quantidade']}")
      voltar_menu()
      return
  else:
    print("Produto fora de estoque ou Inexistente na Prateleira")
    time.sleep(4)
    voltar_menu()
  

def voltar_menu():
    input("\nPressione ENTER para voltar ao menu...")
    Inicio()


def Comprar():
  #Comprar
  valor_compra = float (0)
  while True:
    limpar_tela()
    print("#Compra")
    print("Digite o remédio desejado:")
    for i, remedio in enumerate(dicionario_dados, start=1):
      print(f"{i} - {remedio['Nome Remédio']} (Qtd: {remedio['Quantidade']})")
      print("-------------------") 
    print("s - SAIR")
    print("-------------------")
    try:
      opcao = (input("Digite uma opção:\n-------------------"))
      if opcao.lower() in ("s", "sair"):
        voltar_menu()
      opcao = int(opcao)
      quantidade = int(input("Digite a quantidade:"))
      remedio_escolhido = dicionario_dados [opcao -1]
      if quantidade > 0 and quantidade <= remedio_escolhido['Quantidade']:
       remedio_escolhido['Quantidade'] -= quantidade
       valor_compra += remedio_escolhido["Valor"]*quantidade

       comprar_outro_remedio = int(input("Deseja Comprar Outro Rémedio: /nSIM - 1/nNÃO - 2"))
      if comprar_outro_remedio == 2:
        print(f"O valor da sua compra é de R${valor_compra:.2f}")
        voltar_menu()
      else:
        time.sleep(3)
        print("Quantidade inválida ou Remédio indisponível")
    except (ValueError,IndexError):
      time.sleep(3)
      print("Opção Invalída")



def Remover():
  print("#Remover Estoque do Produto")
  for i, remedio in enumerate(dicionario_dados, start=1):
    print(f"{remedio['id_produto']} - {remedio['nome']} -- Quant = {remedio['quantidade']}")
    print("-------------------") 
  print("s - SAIR")
  print("-------------------")
  opcao = (input("Digite uma opção:\n-------------------"))
  if opcao.lower() in ("s", "sair"):
    voltar_menu()
  opcao = int(opcao)
  quantidade = int(input("Digite a quantidade:"))
  remedio_escolhido = dicionario_dados [opcao -1]
  remedio_escolhido["Quantidade"] -= quantidade
  #atualizar_planilha()
  voltar_menu()
def add_estoque():
  print("#Adicionar Estoque")
  global dicionario_dados
  for remedio in dicionario_dados:
    print(f"{remedio["id_produto"]} - {remedio["nome"]} -- Quant = {remedio["quantidade"]}")
  try:
    id_produto = int(input("Digite o ID do produto: "))
    quantidade_add = int(input("Digite a quantidade a adicionar: "))

    if quantidade_add <= 0:
      print("Quantidade inválida")
      voltar_menu()
      return
    produto_encontrado = None
    for produto in dicionario_dados:
      if produto["id_produto"] == id_produto:
        produto_encontrado = produto
        break
    if not produto_encontrado:
      print("Produto não encontrado")
      voltar_menu()
      return
    nova_quantidade = produto_encontrado["quantidade"] + quantidade_add
 
    sql = "UPDATE produtos SET quantidade = %s WHERE id_produto = %s"
    cursor.execute(sql, (nova_quantidade, id_produto))
    conn.commit()
    # Atualiza os dados em memória ⬇️
  
    cursor.execute("SELECT * FROM produtos")
    dicionario_dados = cursor.fetchall()
    
    print("Estoque atualizado com sucesso!")
    voltar_menu()
  except ValueError:
    print("Digite apenas números")
    voltar_menu()
  
def adicionar_produto():
    print("#Adionar Produto")
    nome_novo_produto = input("Digite o nome do novo produto:\n")
    for produto in dicionario_dados:
        if nome_novo_produto.lower() == produto['nome'].lower():
            print("Produto ja existente no banco de dados")
            return 
    quantidade_novo_produto = int(input("Digite a quantidade:"))
    if quantidade_novo_produto < 0:
        print("Você não pode adiconar números negativos")
        return 
    preco_novo_produto = float(input("Digite o preço do produto:"))
    if preco_novo_produto <= 0:
        print("Você não pode adicionar um produto com um valor de R$0, nem negativo ")
        return 
    limpar_tela()
    print("Produto cadastrado com sucesso")
    voltar_menu()
    dados = (nome_novo_produto, quantidade_novo_produto, preco_novo_produto)
    inserir_dados(dados)
    Inicio()


def inserir_dados(dados):
  global dicionario_dados
  sql = "INSERT INTO produtos (nome,quantidade,preco) VALUES (%s, %s, %s)"
  cursor.execute(sql,dados)
  conn.commit()
  cursor.execute("select * from produtos")
  dicionario_dados = cursor.fetchall()


def remover_produto():
  global dicionario_dados
  print("#Remover Produto")
  # Printa cada produto ⬇️
  for produto in dicionario_dados:
    print(f"{produto['id_produto']} - {produto['nome']}")
  #Da input no produto que vai ser removido ⬇️
  produto_a_ser_removido = int(input("Digite o número ao lado do produto que deseja remover:\n"))

  #Trata para ver se o número do produto digitado exite ⬇️
  ok = False
  for produto in dicionario_dados:
    if produto_a_ser_removido == produto['id_produto']:
      ok = True
      break
  if ok == False:
    print("Produto não encontrado")
    voltar_menu()
    return

  #Remove o produto do banco de dados e salva ⬇️
  sql = "DELETE FROM produtos WHERE id_produto = %s"
  cursor.execute(sql, (produto_a_ser_removido,))
  conn.commit()
  limpar_tela()
  print("Produto removido com sucesso")
  
  # Atualiza os dados em memória ⬇️
  
  cursor.execute("SELECT * FROM produtos")
  dicionario_dados = cursor.fetchall()
  voltar_menu()

Inicio()


