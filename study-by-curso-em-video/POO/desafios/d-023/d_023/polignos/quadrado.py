from d_023.polignos import Poligno

class Quadrado(Poligno):
    def __init__(
        self,
        comprimento_do_lado: int = 1
    ):
        super().__init__(
            4
        )

        self.comprimento_do_lado = comprimento_do_lado

    def perimetro(self) -> float:
        return self.quantidade_de_lados * self.comprimento_do_lado

    def area(self) -> float:
        return self.comprimento_do_lado ** 2