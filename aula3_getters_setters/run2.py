class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None
    
    def setter(self, valor: int) -> None: # Definir 
        self.__valor = valor

    @property
    def getter(self) -> int: # Pegar/Obter
        return self.__valor

    
my_class = MinhaClasse()
my_class.setter(123)
print(my_class.getter)