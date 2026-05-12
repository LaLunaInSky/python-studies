from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from d_025.transportes.moto import Moto
from d_025.transportes.caminhao import Caminhao
from d_025.transportes.drone import Drone

class TabelaDePreco:
    def __init__(self):
        pass

    def fretes(
        self,
        distancia_da_entrega: int = 1
    ):
        console = Console()

        table = Table()

        table.add_column("Distância")
        table.add_column("Tipo")
        table.add_column("Frete")

        entregas = [
            Moto(distancia_da_entrega),
            Caminhao(distancia_da_entrega),
            Drone(distancia_da_entrega)
        ]

        for entrega in entregas:
            table.add_row(
                f"{distancia_da_entrega}Km",
                entrega.__class__.__name__,
                entrega.calcularFrete()
            )

        panel = Panel(
            table,
            title="Tabela de Fretes",
            expand=False
        )

        console.print(panel)
        console.print()