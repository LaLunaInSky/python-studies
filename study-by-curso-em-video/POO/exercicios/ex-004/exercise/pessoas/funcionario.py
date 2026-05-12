from exercise.pessoas import Pessoa

from rich.console import Console

class Funcionario(Pessoa):
    def __init__(
        self,
        nome: str,
        idade: int,
        cargo: str,
        setor: str
    ):
        super().__init__(
            nome,
            idade
        )
        
        self.cargo = cargo
        self.setor = setor

    def baterPonto(self):
        console = Console()

        console.print(
            f"O(a) funcionário(a) {self.nome} acabou de bater o ponto"
        )