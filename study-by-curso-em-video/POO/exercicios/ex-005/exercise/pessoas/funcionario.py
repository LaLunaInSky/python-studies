from exercise.pessoas import Pessoa
from rich.console import Console

class Funcionario(Pessoa):
    console = Console()

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
        self.__class__.console.print(
            f"O(a) funcionário(a) {self.nome} acabou de bater o ponto"
        )

    def estudar(self):
        self.__class__.console.print(
            f"O(a) funcionário(a) {self.nome} se especializa para a área de {self.setor}"
        )