from rich import print
from rich.panel import Panel

class Churrasco():
    # Atributos de Classe
    consumo_padrao:float = 0.400
    preco_kg:float = 82.40

    def __init__(self, titulo="", quantidade=0):
        self.titulo = titulo
        self.quantidade = quantidade

    def __str__(self):
        return f"Esse é {self.titulo} com {self.quantidade} pessoas participando."
    
    def calcular_qtd_carne(self) -> float:
        return self.quantidade * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.quantidade
    
    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]"
        conteudo += f"\nCada participante comerá {self.consumo_padrao}kg e cada kg custa R${self.preco_kg:,.2f}"
        conteudo += f"\nRecomendo comprar {self.calcular_qtd_carne():.3f}kg de carne"
        conteudo += f"\nO custo total será de R${self.calcular_custo_total():,.2f}"
        conteudo += f"\nCada pessoa pagará R${self.calcular_custo_individual():,.2f} para participar"
        caixa = Panel(conteudo, title=self.titulo)
        print(caixa)


c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()   