class AnimaisMarinhos():

    def __init__(self, especie, habitat, tamanho, mortalidade, sexo, nada, mamiferos):
        self.especie = especie
        self.habitat = habitat
        self.tamanho = tamanho
        self.mortalidade = mortalidade
        self.sexo = sexo
        self.nada = nada
        self.mamifero = mamiferos
    
    def nadar(self):
        if self.nada == 'True':
            return print(f"Olá sou um {self.especie} e consigo Nadar")
        else:
            return print(f"Olá sou um {self.especie} e não consigo Nadar")
    
    def respirar_dentro_agua(self):
        if self.mamifero == 'Sim':
            return print(f"{self.especie} não conseguem respirar debaixo de água")
        else:
            return print(f"{self.especie} consegue respirar debaixo da água")


        

    


        