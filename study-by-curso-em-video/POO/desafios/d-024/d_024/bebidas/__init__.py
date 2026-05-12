from abc import ABC, abstractmethod
from rich.console import Console
from rich.panel import Panel

class BebidaQuente(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def misturar(self) -> str:
        pass

    @abstractmethod
    def servir(self) -> str:
        pass

    def ferverAgua(self) -> str:
        return "Fervendo a água a 100 graus Celsius."
    
    def preparar(self):
        console = Console()
        
        conteudo_do_panel = f"1. {self.ferverAgua()}\n"

        conteudo_do_panel += f"2. {self.misturar()}\n"
        
        conteudo_do_panel += f"3. {self.servir()}"

        panel = Panel(
            conteudo_do_panel,
            title=f"Iniciando o Preparo do {self.__class__.__name__}",
            subtitle=f"Bebida Pronta",
            expand=False
        )

        console.print(panel)