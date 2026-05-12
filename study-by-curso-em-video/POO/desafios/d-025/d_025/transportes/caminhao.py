from d_025.transportes import Transporte

class Caminhao(Transporte):
    def __init__(
        self,
        distancia_da_entrega: int = 50
    ):
        super().__init__(
            distancia_da_entrega,
            1.20
        )

        self.distancia_minima = 50

    def calcularFrete(self) -> str:
        if self.distancia_da_entrega < self.distancia_minima:
            self.preco_frete = 0.0

            return "Raio mínimo de 50Km"
        else:
            self.preco_frete = self.distancia_da_entrega * self.valor_do_km

            return f"R${self.preco_frete:.2f}"