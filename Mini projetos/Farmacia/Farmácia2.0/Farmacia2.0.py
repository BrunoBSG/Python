import os
import time
import pandas as pd
caminho = "D:\Projetos\Workspace Python\Mini projetos\Farmácia2.0\DADOS_FARMACIA.xlsx"
DataFrame = pd.read_excel(caminho)
dicionario_dados = DataFrame.to_dict(orient="records")

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
6 - Sair
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
      case 6:
        #Sair
        limpar_tela()
        atualizar_planilha()
        print("Programa Finalizado")
        time.sleep(3)
        exit()
      case 4:
       #Adicionar Estoque ao Produto
       limpar_tela()
       add()
      case 5:
        #Remover Estoque ao Produto
        limpar_tela()
        Remover()
      case _:
        #Caso Der Algum erro no input
        print("Erro")
        time.sleep(2)
        voltar_menu()
def Verificar_Todos_Remedios():
  #Verificar Todos os remedios
  print("Lista de Remédios:\n-------------------")
  for remedio in dicionario_dados:
    print(f"{remedio["Nome Remédio"]}: {remedio["Quantidade"]}")
    print("-------------------")
  voltar_menu()
def Pesquisa():
  #Pesquisar Remedios
  nome_pesquisado = input("Digite o nome a ser pesquisado:\n ")
  for remedio in dicionario_dados:
    if nome_pesquisado.lower().strip() == remedio["Nome Remédio"].lower().strip() and remedio["Quantidade"] > 0:
      limpar_tela()
      print("Produto está em Estoque")
      print(f"Quantidade em estoque: {remedio['Quantidade']}")
      voltar_menu()
      return
  else:
    print("Produto fora de estoque ou Inexistente na Prateleira")
    time.sleep(4)
    voltar_menu()
  
def Mostrar_remedios():
  for remedio in dicionario_dados:
    print(f"{remedio["Nome Remédio"]}")
    print("-------------------")
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
       atualizar_planilha()
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
def atualizar_planilha():
  df = pd.DataFrame(dicionario_dados)
  df.to_excel(caminho, index=False)


def Remover():
  print("#Remover Estoque do Produto")
  for i, remedio in enumerate(dicionario_dados, start=1):
    print(f"{i} - {remedio['Nome Remédio']} (Qtd: {remedio['Quantidade']})")
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
  atualizar_planilha()
  voltar_menu()
def add():
  print("#Adicionar Estoque")
  for i, remedio in enumerate(dicionario_dados, start=1):
    print(f"{i} - {remedio['Nome Remédio']} (Qtd: {remedio['Quantidade']})")
    print("-------------------") 
  print("s - SAIR")
  print("-------------------")
  opcao = (input("Digite uma opção:\n-------------------"))
  if opcao.lower() in ("s", "sair"):
    voltar_menu()
  opcao = int(opcao)
  quantidade = int(input("Digite a quantidade:"))
  remedio_escolhido = dicionario_dados [opcao -1]
  remedio_escolhido["Quantidade"] += quantidade
  atualizar_planilha()
  voltar_menu()
Inicio()