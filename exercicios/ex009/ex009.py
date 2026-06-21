class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo protected (#)

    # Métodos Acessores
    def get_nota(self): # Método Getter (Get = pegar)
        return self._nota

    def set_nota(self, valor): # Método Setter (Set = Configurar, Definir)
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota Inválida!")