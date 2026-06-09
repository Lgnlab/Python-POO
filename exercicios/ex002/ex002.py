# Declaração de Classe
class Gafanhoto:
    """
Essa classe cria um Gafabhoto, que é uma pessoa que tem nome e idade.

Para criar uma nova pessoa, use
Variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "", idade = 0):   # Método construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): # Personaliza o retorno dos dados(Subescreve o endereço da memória) permitindo um print direto no objeto
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"
    
    def __getstate__(self): # Personaliza o estado
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaração de Objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1.__dict__) # Atributo
print(g1.__getstate__()) # Método
print(g1.__class__) # Mostra a classe


g2 = Gafanhoto("Mauro", 53)
g2.aniversario()
print(g2.__getstate__())

