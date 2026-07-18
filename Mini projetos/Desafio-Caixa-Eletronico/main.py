try:
    valor_usuario_deseja_sacar = int(input("Digite o valor que deseja sacar"))

    qtn_100 = 0
    qtn_50 = 0
    qtn_20 = 0
    qtn_10 = 0
    qtn_5 = 0
    qtn_2 = 0

    if valor_usuario_deseja_sacar >= 100:
        qtn_100 = valor_usuario_deseja_sacar // 100
        valor_usuario_deseja_sacar -= qtn_100*100

    if valor_usuario_deseja_sacar >= 50:
        qtn_50 = valor_usuario_deseja_sacar // 50
        valor_usuario_deseja_sacar -= qtn_50*50
    
    if valor_usuario_deseja_sacar >= 20:
        qtn_20 = valor_usuario_deseja_sacar // 20
        valor_usuario_deseja_sacar -= qtn_20*20
    
    if valor_usuario_deseja_sacar >= 10:
        qtn_10 = valor_usuario_deseja_sacar // 10
        valor_usuario_deseja_sacar -= qtn_10*10
    
    if valor_usuario_deseja_sacar >= 5:
        qtn_5 = valor_usuario_deseja_sacar // 5
        valor_usuario_deseja_sacar -= qtn_5*5
    
    if valor_usuario_deseja_sacar >= 2:
        qtn_2 = valor_usuario_deseja_sacar // 2
        valor_usuario_deseja_sacar -= qtn_2*2
    if valor_usuario_deseja_sacar > 0:
        print("Nãofoi possível montar o saque exatamente.")

    print("\nNotas entregues:")
    print(f"{qtn_100} nota(s) de R$100")
    print(f"{qtn_50} nota(s) de R$50")
    print(f"{qtn_20} nota(s) de R$20")
    print(f"{qtn_10} nota(s) de R$10")
    print(f"{qtn_5} nota(s) de R$5")
    print(f"{qtn_2} nota(s) de R$2")



except ValueError:
    print("Digite apenas números inteiros.")
