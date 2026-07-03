class MinhaClasse():
    def __init__(self, info, elem): # metodo construtor
        self.atributo_1 = "meu atributo"
        self.atributo_2 = elem
        self.atributo_3 = [1, 2, "a"]
        self.atributo_novo = info
        print(self.atributo_novo)

    def metodo_1(self):
        print("minha ação1")
        print("minha ação2")
        return "Ola Mundo"

    def metodo_2(self, numero):
        print(self.atributo_3[1] + numero)

# Objeto      # Classe -> instanciamos um objeto
minha_classe = MinhaClasse("info aqui no construtor")

response = minha_classe.metodo_1()
print(response)
minha_classe.metodo_2(3)