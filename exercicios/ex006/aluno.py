from pessoa import Pessoa

class Aluno(Pessoa):  # CRIANDO A RELAÇÃO ENTRE CLASSES(HERANÇA)
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade) # CHAMA A CLASSE MÃE
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matricula")