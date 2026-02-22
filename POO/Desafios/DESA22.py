class Controle_Remoto:
    def __init__(self):
        self.comando = ""
        self.canal_atual = 1
        self.voloume_atual = 0
        self.on_off = "off"
    
    def status (self):
        print(f"\nA tv está {self.on_off}\n<CH{self.canal_atual}>\n_VOL{self.voloume_atual}+")

    def ligar(self):
        if self.comando == "@":
            if self.on_off == "off":
                self.on_off = "on"
            else:
                self.on_off = "off"



    def aumentar_volume(self):
        if self.comando == "+" and self.voloume_atual < 10 and self.on_off == "on":
           self.voloume_atual += 1
    

    def diminuir_volume(self):
        if self.comando == "-" and self.voloume_atual > 0 and self.on_off == "on":
            self.voloume_atual -= 1
            
    def aumentar_canal(self):
        if self.comando == ">" and self.canal_atual < 5 and self.on_off == "on":
           self.canal_atual += 1
    
    def diminuir_canal(self):
        if self.comando == "<" and self.canal_atual > 0 and self.on_off == "on":
           self.canal_atual -= 1
    
    def all(self, comma):
        self.comando = comma

        
        self.ligar()
        self.aumentar_volume()
        self.diminuir_volume()
        self.aumentar_canal()
        self.diminuir_canal()

controle = Controle_Remoto()

while True:
    controle.status()
    inputt = input()
    controle.all(inputt)
    if inputt == "e":
        print("Tv desligada da tomada!")
        break
    