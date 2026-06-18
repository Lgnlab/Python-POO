from abc import ABC, abstractmethod

# CLASSE MÃE
class Transporte(ABC):
    def __init__(self, distancia): 
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass

# CLASSES FILHAS 
class Moto(Transporte):
    fator = 0.50
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = self.distancia * Moto.fator()
        return f"R${self.frete:.2f}"

class Caminhao(Transporte):
    fator = 1.20
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > 50:
            return f"R${self.distancia * Caminhao.fator:.2f}"
        else:
            self.frete = 0
            return "Raio mínimo de 50km"

class Drone(Transporte):
    fator = 9.50
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia <= 10:
            return f"R${self.distancia * Drone.fator:.2f}"
        else:
            self.frete = 0
            return "Raio máximo de 10km"