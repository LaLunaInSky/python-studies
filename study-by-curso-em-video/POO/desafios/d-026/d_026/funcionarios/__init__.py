from abc import ABC, abstractmethod
from rich.console import Console
from rich.panel import Panel

class Funcionario(ABC):
    salario_minimo = 1621.0
    inss = 7.5

    def __init__(
        self,
        nome: str = "Fulano",
        salario_bruto : float = 0.0
    ):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario = 0.0

    @abstractmethod
    def calcularSalario(self):
        pass

    def analisarSalario(self):
        console = Console()

        conteudo_do_panel = f"O salário de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de R${self.salario:.2f} e corresponde a[yellow] {self.salario / self.__class__.salario_minimo:.1f} salários mínimos[/]."

        panel = Panel(
            conteudo_do_panel,
            title="Análise de Salário",
            expand=False,
            width=50
        )

        console.print(panel)
        console.print()