from d_025.transportes import Transporte

class Drone(Transporte):
    def __init__(
        self,
        distancia_da_entrega: int = 1
    ):
        super().__init__(
            distancia_da_entrega,
            9.50
        )

        self.distancia_maxima = 10

    def calcularFrete(self) -> str:
        if self.distancia_da_entrega > self.distancia_maxima:
            self.preco_frete = 0.0

            return "Raio máximo de 10Km"
        else:
            self.preco_frete = self.distancia_da_entrega * self.valor_do_km

            return f"R${self.preco_frete:.2f}"