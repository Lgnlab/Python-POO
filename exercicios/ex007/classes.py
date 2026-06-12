from abc import ABC, abstractmethod # Abstract Base Classes

# Classe Mãe (SUPERCLASSE)
class Pessoa(ABC): # Classe Abstrata
    # NÃO PODE SER UM OBJETO
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade
    
    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self): # Não coloca a programação do método na mãe, só nos filhos
        pass

# Subclasses de Pessoa (FILHOS)
class Aluno(Pessoa):  # CRIANDO A RELAÇÃO ENTRE CLASSES(HERANÇA)
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade) # CHAMA A CLASSE MÃE
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matricula")
    
    def estudar(self): 
        print(f"{self.nome} está estudando {self.curso} na turma {self.turma}")



class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"Prof. {self.nome} começou a dar aula")

    def estudar(self):
        print(f"{self.nome} é especialista em {self.especialidade} no {self.nivel}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} acabou de bater ponto")

    def estudar(self):
        print(f"{self.nome} se especializa para a área de {self.setor}")