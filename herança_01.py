class Personagem():
    def __init__(self, nome: str, filme: bool, roupa: str, serie: bool, genero: str,  jogo: bool ):
        self.roupa = roupa
        self.serie = serie
        self.nome = nome
        self.filme = filme
        self.genero = genero
        self.jogo = jogo

    def Tema(self):
        print(f"O personagem {self.nome} participa de um filme/serie de genero {self.genero}")
    
    def Existe(self):
        print(f"O personagem {self.nome} não existe na vida real")

    def Filme_Game(self):
        print(f"{self.nome} é de um filme")

        