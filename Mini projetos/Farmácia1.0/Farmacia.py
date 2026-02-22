import os
import time
#Remédios Que a Farmacia Possui
Remedio1 = {"Nome" : "Ibuprofeno 600MG", "Quantidade" : 49, "Valor" : 24.99 }
Remedio2 = {"Nome" : "Loratadina 10MG", "Quantidade" : 46, "Valor" : 12.99 }
Remedio3 = {"Nome" : "Lozartana 50MG", "Quantidade" : 9, "Valor" : 14.49 }
Remedio4 = {"Nome" : "Epocler", "Quantidade" : 17, "Valor" : 4.48 }
Remedio5 = {"Nome" : "Pantoprazol 40MG", "Quantidade" : 21, "Valor" : 21.47 }

RemedioS = (Remedio1, Remedio2, Remedio3,Remedio4,Remedio5)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Inicio
def Pagina_Inicial():
  try:
    limpar_tela()
    opcao = int(input("\nDigite uma opção:\n-------------------\nPesquisar Remédios - 1\nVerificar Todos os Remédios - 2\nComprar - 3\nEncerrar - 4"))

    match opcao:
        case 1:
          limpar_tela()
          print("Remédios")
          for remedio in RemedioS:
            print(remedio["Nome"])
            print("-------------------")
          Pesquisa(input("Digite o Nome do Remédio:"))
        case 2:
          limpar_tela()
          Verificar_Remedios()
        case 3:
          limpar_tela()
          Comprar()
        case 4:
            return
        case _:
          limpar_tela()
          print("Opção inválida")

  except ValueError:
      print("Erro: digite apenas números")

#Pesquisa CASE 1
def Pesquisa(Nome_a_ser_Pesquisado):
  limpar_tela()
  print("#Pesquisa")
  for remedio in RemedioS:
    if Nome_a_ser_Pesquisado.lower().strip() == remedio["Nome"].lower() and remedio["Quantidade"] > 0:
      limpar_tela()
      print("Produto está em Estoque")
      print(f"Quantidade em estoque: {remedio['Quantidade']}")
      time.sleep(3)
      Pagina_Inicial()
      return
  else:
    print("Produto fora de estoque ou Inexistente na Prateleira")
    time.sleep(3)
    Pagina_Inicial()
#Verificar Todos os Rémedios em estoque CASE 2
def Verificar_Remedios():
  for remedio in RemedioS:
    if remedio["Quantidade"] > 0:
      print(remedio["Nome"])
      print(f"Qantidade: {remedio['Quantidade']}")
      print("-------------------")
    else:
      print(f"O remédio {remedio['Nome']} está forá de estoque.")
      print("-------------------")
  time.sleep(5)
  Pagina_Inicial()
 #Comprar CASE 3
def Comprar():
  valor_compra = float (0)
  while True:
    limpar_tela()
    print("#Compra")
    print("Digite o remédio desejado:")
    for i, remedio in enumerate(RemedioS, start=1):
      print(f"{i} - {remedio['Nome']} (Qtd: {remedio['Quantidade']})")
      print("-------------------") 
    print("12 - SAIR")
    print("-------------------")
    try:
      opcao = int(input("Digite uma opção:\n-------------------"))
      if opcao == 12:
        Pagina_Inicial()
      quantidade = int(input("Digite a quantidade:"))
      remedio_escolhido = RemedioS [opcao -1]
      valor_compra += remedio_escolhido["Valor"]*quantidade
      if quantidade > 0 and quantidade <= remedio_escolhido['Quantidade']:
       remedio_escolhido['Quantidade'] -= quantidade
       comprar_outro_remedio = int(input("Deseja Comprar Outro Rémedio: /nSIM - 1/nNÃO - 2"))
      if comprar_outro_remedio == 2:
        print(f"O valor da sua compra é de R${valor_compra:.2f}")
        time.sleep(4)
        Pagina_Inicial()
      else:
        time.sleep(3)
        print("Quantidade inválida ou Remédio indisponível")
    except (ValueError,IndexError):
      time.sleep(3)
      print("Opção Invalída")
Pagina_Inicial()