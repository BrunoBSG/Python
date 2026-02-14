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


c1 = ContaBancaria("Mario", 30000)
print(c1)
