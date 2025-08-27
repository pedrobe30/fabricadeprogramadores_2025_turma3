class Pessoa():
    
    def __init__(self, nome: str, estado_profissional: bool, idade: int, _contabancaria: float, _endereco: list, _senha_cartao: int, __email: str, __celular: int, _cpf: int, altura, _senha: str ):
        self.nome = nome
        self.estado_profisional = estado_profissional
        self.idade = idade
        self._contabacaria = _contabancaria
        self._endereco = _endereco
        self._senha_cartao = _senha_cartao
        self.__email = __email
        self.__celular = __celular
        self._cpf = _cpf
        self.altura = altura
        self._senha = _senha

     
    
    
    def CadastrandoEmail(self):
        self.__email = input("Digite seu email")

     



    

