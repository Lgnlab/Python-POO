class Termostato:
    def __init__(self):
        self.__temperatura = 24 # Atributo Privado

    # Criando Atributo Validável
    @property
    def temperatura(self): # Acessar
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor): # Configura/alterar
        if valor % 0.5 != 0:
            raise ValueError(f"Temperatura de {valor} é inválida!")
        if valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.ftemperatura = 30
        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"