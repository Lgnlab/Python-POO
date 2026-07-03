class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.cpf = cpf

    def apresentar(self):
        print(f"Ola! Minha altura - {self.altura}")
        self.__coletar_documento()

    def __coletar_documento(self):
        print(f"Meu documento - {self.cpf}")
    

jorge = Pessoa("1.70", "000.000.000-00")
jorge.__coletar_documento()