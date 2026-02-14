class Pessoa:
    """
    Funciona para gerar uma pessoa com nome e idade
    e tem o metodo Aniversario() que A pessoa ou
    objeto faz aniversario adicionando mais um a idade.
    """
    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome
    #⬇️Quando voce da print na pessoa (Objeto) voce imprime mais bonito⬇️
    def __str__(self):
        return f"Nome: {self.nome} \nIdade: {self.idade}"
    #⬇️A pessoa ou objeto faz aniversario adicionando mais um a idade⬇️
    def Aniversario(self):
        self.idade += 1
p1 = Pessoa(15, "Maria Clara")
print(p1)
p2 = Pessoa(23, "Laura")
print(p2)