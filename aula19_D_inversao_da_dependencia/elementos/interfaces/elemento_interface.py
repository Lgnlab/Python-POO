from abc import ABC, abstractmethod

class Elemento(ABC):

    @abstractmethod
    def executar(self) -> None: pass