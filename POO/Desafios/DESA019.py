class Livro:
    def __init__(self,nome , qtn):
        self.nome_livro = nome
        self.Quantidade_De_Paginas = qtn
        self.pagina_atual = 0

    def avançar_pagina(self, qtn_paginas_avancadas):
        if qtn_paginas_avancadas <= self.Quantidade_De_Paginas:
            while self.pagina_atual < qtn_paginas_avancadas:
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual}    ")
            print(f"Você avançou {qtn_paginas_avancadas} páginas\ne agora está na página {self.pagina_atual} ")
        elif qtn_paginas_avancadas > self.Quantidade_De_Paginas:
            print("Você não pode avançar está quantidade de páginas")
l1 = Livro("Harry Potter", 100)
l1.avançar_pagina(5)
#Saída⬇️
#Pág1    
#Pág2    
#Pág3
#Pág4
#Pág5
#Você avançou 5 páginas
#E agora está na página 5