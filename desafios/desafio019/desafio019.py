from rich import print

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f":open_book: Você acabou de abir o livro [blue]'{self.titulo}'[/] que tem [red]{self.paginas} páginas no total[/]. Você agora está na página [green]{self.pagina_atual}[/]")

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward: ", end='')
                cont += 1
        print(f"Você avançou [blue]{cont}[/] páginas e agora está na página [green]{self.pagina_atual}[/]")
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")

    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.paginas else False

l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(20)          