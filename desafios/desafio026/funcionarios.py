from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

# CLASSE MÃE
class Funcionario(ABC):
    sal_min = 1_612
    inss = 7.5
    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        conteudo = f"O salário de {self.nome} ({self.__class__.__name__}) é de R${self.salario:.2f} e corresponde a {self.salario / Funcionario.sal_min:.1f} salários mínimos."
        painel = Panel(conteudo, title="Análise de Salário", width=50)
        print(painel)

# CLASSES FILHOS
class Horista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, qtd_horas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas
        self.sal_bruto = self.valor_hora * self.qtd_horas

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto = Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto
    
    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)
