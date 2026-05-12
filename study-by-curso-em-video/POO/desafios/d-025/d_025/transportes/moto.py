from d_025.transportes import Transporte

class Moto(Transporte):
    def __init__(
        self,
        distancia_da_entrega: int = 1
    ):
        super().__init__(
            distancia_da_entrega,
            0.50
        )

    def calcularFrete(self) -> str:
        self.preco_frete = self.distancia_da_entrega * self.valor_do_km

        return f"R${self.preco_frete:.2f}"