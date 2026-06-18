from abc import ABC, abstractmethod
import math

# CLASSE MÃE
class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.lados = qtd_lados
    
    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

# CLASSES FILHAS
class Quadrado(Poligono):
    def __init__(self, qtd_lados = 1):
        super().__init__(4)
        self.lado = qtd_lados

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * self.raio ** 2 