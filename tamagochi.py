class Tamagochi:
    def __init__(self,nome:str,tipo:str,vida_maxima:int,energia_maxima:int):
        self.nome = nome 
        self.tipo = tipo
        self.vida_maxima = vida_maxima
        self.energia_maxima = energia_maxima
        self.vida_atual = 100
        self.energia_atual = 100
        
    def brincar(self):
        if self.energia_atual > 0:
            self.energia_atual -= 25
            return f"O(a) {self.nome} brincou e gastou 25 de energia. Energia {self.energia_atual} Saúde {self.vida_atual}."
            
    def comer(self):
        if self.energia_atual >= self.energia_maxima:
            return f"A energia já está em 100%. Energia {self.energia_atual} Saúde {self.vida_atual}."
        elif self.energia_atual < self.energia_maxima:
            self.energia_atual += 50
            if self.energia_atual == self.energia_maxima:
                return f"A energia já está no máximo."
            else:
                return f"Após comer uma tapioca o {self.tipo}. Energia {self.energia_atual} Saúde {self.vida_atual}."
            
    def trabalhar(self):
        if self.energia_atual < 0:
            return f"O(a) {self.tipo} {self.nome} não tem energia o suficiente. Energia {self.energia_atual} Saúde {self.vida_atual}."
        elif self.energia_atual > 30:  
            self.energia_atual -= 30
            self.vida_atual -= 5
            return f"Energia e vida foram gastas para trabalhar e o {self.nome} recebeu uma tapioca. Energia {self.energia_atual} Saúde {self.vida_atual}."
        
    def dormir(self):
        if self.energia_atual == 0:
            self.energia_atual = self.energia_maxima
            self.vida_atual -= 30
            self.vida_atual += 10
            return f"O(a) desmaiou de cansaço. Após o descanso recuperou 100% de energia e 10 vida, mesmo tendo perdido 30 de vida. Energia {self.energia_atual} Saúde {self.vida_atual}."
        elif self.energia_atual == 100:
            return f"O(a) está muito disposto, vá brincar!!! (ou lutar 😈😈) Energia {self.energia_atual} Saúde {self.vida_atual}."
        
        elif self.energia_atual > 50:
            self.energia_atual = self.energia_maxima
            return f"O(a) não está tão cansado, mas foi dormir. Energia {self.energia_atual} Saúde {self.vida_atual}."
        
        elif self.energia_atual > 0:
            self.energia_atual = self.energia_maxima
            return f"O(a) está ficando cansado e foi dormir. Energia {self.energia_atual} Saúde {self.vida_atual}."
        
    def lutar(self):
        if self.vida_atual == 0:
            return f"💀💀💀💀💀 Puts 💀💀💀💀💀"
        if self.energia_atual == 0:
            return f"O(a {self.nome} desmaiou de cansaço.)"
        if self.vida_atual < 100 or self.vida_atual > 20:
            if self.energia_atual >= 30:
                self.vida_atual -= 20
                self.energia_atual -= 30
                return f"O(a) está pronto para lutar. Ele lutou ficou com {self.vida_atual} de vida. Energia {self.energia_atual} Saúde {self.vida_atual}."
            else:
                return "Não há enrgia suficiente."
        elif self.vida_atual < 20 or self.energia_atual < 30:
            return f"O(a) não está apto a lutar no momento, descanse ou visite a enfermaria. Energia {self.energia_atual} Saúde {self.vida_atual}."
        
    def irEnfermaria(self):
        if self.vida_atual == self.vida_maxima:
            return f"O(a) {self.nome} está bem de saúde, vá arranjar o que fazer."
        
        elif self.vida_atual < self.vida_maxima:
            self.energia_atual == self.energia_maxima
            return f"O(a) {self.nome} descansou e agora está 100% saudável. Energia {self.energia_atual} Saúde {self.vida_atual}."

        
tama1 = Tamagochi(nome="Thales", tipo="Rabilho", vida_maxima=100, energia_maxima= 100.)

print(tama1.brincar())
print(tama1.comer())
print(tama1.lutar())
print(tama1.trabalhar())
print(tama1.irEnfermaria())
print(tama1.lutar())
print(tama1.trabalhar())
print(tama1.comer())
print(tama1.brincar())
print(tama1.dormir())




        
            
        
        
            
            
        