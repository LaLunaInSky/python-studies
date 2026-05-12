from abc import ABC, abstractmethod
from rich.console import Console
from rich.panel import Panel

class Poligno(ABC):
    def __init__(
        self,
        quantidade_de_lados: int = 0
    ):  
        self.quantidade_de_lados = quantidade_de_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

    def dados(self):
        console = Console()

        conteudo_do_panel = f"Perímetro = {self.perimetro():.1f}\n"

        conteudo_do_panel += f"Área = {self.area():.1f}"

        panel = Panel(
            conteudo_do_panel,
            title=f"Dados do {self.__class__.__name__}",
            expand=False
        )

        console.print(panel)