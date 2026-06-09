from rich import print

class Funcionario:
    """
    -Essa classe cria um funcionário que tem nome, setor e carga.
    Para criar um novo funcionário informe nome, setor e idade.
    """
    # Atributos de Classe
    empresa = "Curso em Vídeo"
    def __init__(self, nome = "", setor = "", cargo = ""):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentar(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}"



c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentar())


c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentar())