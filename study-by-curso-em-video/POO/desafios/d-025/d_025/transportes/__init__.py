from abc import ABC, abstractmethod
from rich.console import Console

class Transporte(ABC):
    def __init__(
        self,
        distancia_da_entrega: int = 1,
        valor_do_km: float = 0.1
    ):
        self.distancia_da_entrega = distancia_da_entrega

        self.valor_do_km = valor_do_km

        self.preco_frete = 0.0


    @abstractmethod
    def calcularFrete(self) -> str:
        pass

    def analisarFrete(self):
        console = Console()

        console.print(
            f"Frete de {self.__class__.__name__} para {self.distancia_da_entrega}Km = {self.calcularFrete()}\n"
        )