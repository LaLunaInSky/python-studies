from d_024.bebidas.cafe import Cafe
from d_024.bebidas.cha import Cha
from d_024.bebidas.leite import Leite

def main():
    bebida_01 = Cafe()
    bebida_01.preparar()

    print()

    bebida_02 = Cha()
    bebida_02.preparar()

    print()

    bebida_03 = Leite()
    bebida_03.preparar()