from rich import print
from rich.panel import Panel

caixa = Panel('Esse aqui é um painel de exemplo', title='Mensagem', style='red', width=35, height=15)

print(caixa)