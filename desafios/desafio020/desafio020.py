from rich import print
from rich.panel import Panel

class Gamer():
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, jogos):
        self.favoritos.append(jogos)
        self.favoritos = sorted(self.favoritos, key=str.lower) # key usado como criterio de ordenação(letras minusculas)

    def ficha(self):
        conteudo = f"Nome real: {self.nome}"
        conteudo += f"\nJogos favoritos:"
        for game in self.favoritos:
            conteudo += f"\n{game}"
        painel = Panel(conteudo, title=f"Jogador: {self.nick}", width=40)
        print(painel)
        


f1 = Gamer("Lucas", "LGN")
f1.add_favoritos("Mario Bros")
f1.add_favoritos("Sonic")
f1.ficha()  