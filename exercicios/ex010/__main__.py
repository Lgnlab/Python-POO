from ex010 import Avaliacao

def main():
    av1 = Avaliacao("Pedro", "Matemática")
    av1.nota = -7.2
    print(f"{av1.nome} tirou {av1.nota} em {av1.disciplina}")


if __name__ == "__main__":
    main()