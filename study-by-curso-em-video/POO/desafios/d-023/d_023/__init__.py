from d_023.polignos.quadrado import Quadrado
from d_023.polignos.circulo import Circulo

def main():
    poligno_01 = Quadrado(
        12
    )

    poligno_02 = Circulo(
        20
    )

    poligno_01.dados()
    poligno_02.dados()