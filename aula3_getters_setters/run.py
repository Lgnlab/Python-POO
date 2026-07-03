class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None

    def setter(self, valor: int) -> None: # Definir 
        self.__valor = valor

    def getter(self) -> int: # Pegar/Obter
        return self.__valor

    

my_class = MinhaClasse()
my_class.setter(42)
valor = my_class.getter()
print(valor)