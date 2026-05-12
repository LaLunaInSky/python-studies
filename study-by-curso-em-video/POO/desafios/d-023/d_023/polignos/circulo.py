from d_023.polignos import Poligno
from math import pi

class Circulo(Poligno):
    def __init__(
        self,
        raio: float = 0.0
    ):
        super().__init__(
            0
        )

        self.raio = raio

    def perimetro(self) -> float:
        return 2 * pi * self.raio
    
    def area(self) -> float:
        return pi * (self.raio ** 2)