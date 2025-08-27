from herança_01 import Personagem

class SuperHeroi(Personagem):
    def __init__(self, nome, filme, roupa, serie, genero, poder):
        super().__init__(nome)
        self.poder = poder
    
    def Tema(self):
        print(f"O personagem {self.nome} participa de um filme/serie de genero de Ficção/Fantasia")
    
    def DescobrindoPoder(self):
        print(f"{self.nome} tem poder de {self.poder}")

class AntiHeroi(Personagem):
    def __init__(self, nome, filme, roupa, serie, genero, rival):
        super().__init__(nome)
        self.rival = rival

    def ArquiRival(self):
        print(f"O Vilão {self.nome} tem como Rival o {self.rival}")

class Pessoa(Personagem):
    def __init__(self, nome, filme, ficiticio):
        super().__init__(nome, filme)
        self.ficticio = ficiticio
    
    def Existe(self):
        print(f"Personagem {self.nome} faz o filme {self.filme} mas ele existe na vida real")
    
class Franklin(Personagem):
    
    def Filme_Game(self):
        print(f"{self.nome} na verdade é de um jogo")

