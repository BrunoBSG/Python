import random 

class ContaBancaria:
    """
    Gera uma conta bancaria
    """
    def __init__(self, titular, saldo):
        self.id = random.randint(0, 1000)  
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"A conta com o id: {self.id}\nCom o titular: {self.titular}\nCom o saldo de: R${self.saldo:,.2f}"
    
    def Depositar(self, valor):
        """
        Faz um deposito
        """

        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} realizado com sucesso")


    def Sacar(self,valor):
        """
        Faz um saque
        """

        if (valor <= self.saldo):
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} realizado com sucesso")
        elif valor > self.saldo:
            print("Você não tem saldo suficiente")

        

c1 = ContaBancaria("Mario", 30000)
print(c1) #Mostra o print bonitinho da conta bancaria
c1.Sacar(100000) #Não faz o saque pois não tem saldo na conta
c1.Depositar(10) #Faz um deposito


