import random as r

def inicio():
    print("Bem vindo ao jogo do Cara ou Coroa")
    cara_OU_coroa = r.randint(1,2)
    try:
        
        op1 = int(input("Escolha 1 para Cara e 2 para Coroa: "))
        if op1 not in (1,2):
            print("Opção inválida")
        elif op1 == cara_OU_coroa:
            print("Você Ganhou")   
        else:
                print("Você Perdeu")
    except ValueError: 
        print("Digite Apenas Números")               

while True:
    try:        
        inicio() 
        jogar_novamente = input("\nJogar Novamente s/n".lower())
        if jogar_novamente not in (s,n):
            print("Digite apenas s/n")   
        if jogar_novamente != s:
            print("Fim do")
            break
    except ValueError:
        print("Digite apenas s/n")

         