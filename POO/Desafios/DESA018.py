class Churrasco:
    def __init__(self, nome, qtn):
        self.nomedoChurras = nome
        self.QuantidadeDePessoas = qtn

    def analisar(self):

        #Considerando:
        #Consumo padrão: 400g por pessoa
        #Preço: R$82,40/Kg
        valorDoChurras = 0
        valorDoChurras = (self.QuantidadeDePessoas * 400) / 1000 * 82.40
        return f"O {self.nomedoChurras} é recomendado comprar Kg {self.QuantidadeDePessoas*0.4} de carne\nO total ficará em R${valorDoChurras:,.2f}\nCada pessoa pagará R${valorDoChurras/self.QuantidadeDePessoas:,.2f}"

churras1 = Churrasco("Grande churrasco", 15)
print(churras1.analisar())

#Saída⬇️
#O Grande churrasco é recomendado comprar Kg 6.0 de carne
#O total ficará em R$494.40
#Cada pessoa pagará R$32.96