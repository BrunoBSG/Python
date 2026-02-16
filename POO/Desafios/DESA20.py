class Gamer:
    def __init__(self,nome, nick):
        self.nome = nome
        self.nick = nick
        self.Jogos_favoritos = []
    
    def add_favoritos(self,jogo_favorito):
        self.Jogos_favoritos.append(jogo_favorito)
    
    def ficha(self):
        print(f"Nome real: {self.nome}\nNick:{self.nick}\nJogos favoritos:\n")
        self.Jogos_favoritos.sort()
        for jogo in self.Jogos_favoritos:
            print(f"{jogo}\n")



j1 = Gamer("Bruno","Playerbr")
j1.add_favoritos("Minecraft")
j1.add_favoritos("Brawhalla")
j1.add_favoritos("Ark")
j1.ficha()

#Nome real: Bruno
# Nick:Playerbr   
# Jogos favoritos:

# Ark

# Brawhalla

# Minecraft


j2 = Gamer("Maria Clara","Clarinha")
j2.add_favoritos("Stardew Valley")
j2.add_favoritos("Minecraft")
j2.add_favoritos("The Sims 4")
j2.ficha()

#Nome real: Maria Clara
#Nick:Clarinha
#Jogos favoritos:      

#Minecraft

#Stardew Valley        

#The Sims 4
