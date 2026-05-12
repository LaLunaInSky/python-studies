from rich.console import Console
from rich.panel import Panel

class Produto:
    def __init__(
        self,
        nome: str,
        preco: float
    ):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        console = Console()
        
        conteudo_da_etiqueta = f"{self.nome:^30}\n{"-"*30}\n{f"R${self.preco:,.2f}":.^30}"

        panel = Panel(
            conteudo_da_etiqueta,
            title="Produto",
            expand=False
        )

        console.print(panel)

