# Declaração de Classe
class Gafanhoto:
    def __init__(self):   # Método construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Augusto"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Pedro"
g2.idade = 32
g2.aniversario()
print(g2.mensagem())