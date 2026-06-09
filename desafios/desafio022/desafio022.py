from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 5

    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False
    
    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        pass
    
    def canal_menos(self):
        pass

    def volume_mais(self):
        pass

    def volume_menos(self):
        pass

    def mostrar_tv(self):
        conteudo = ''
        if self.ligado == False:
            conteudo = f"A TV está desligada"
        else:
            conteudo = f"CANAL  = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[black on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "

            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += "[black on cyan] [/]"
                else:
                    conteudo += "[black on white] [/]"
        
        tv = Panel(conteudo, title="[ TV ]", width=30)
        print(tv)


c = ControleRemoto()
c.liga_desliga()
c.mostrar_tv()