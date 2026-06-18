from transporte import *
from rich import print

def main():
    dist = 11

    entrega = Drone(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}km = {entrega.calc_frete()}")
    # {type(objeto).__name__} -> PEGA O NOME DA CLASSE

if __name__ == "__main__":
    main()