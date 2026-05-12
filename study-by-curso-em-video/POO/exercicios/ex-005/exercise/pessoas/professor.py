from exercise.pessoas import Pessoa
from rich.console import Console

class Professor(Pessoa):
    console = Console()

    def __init__(
        self,
        nome: str,
        idade: int,
        especialidade: str,
        nivel: str
    ):
        super().__init__(
            nome,
            idade
        )
        
        self.especialidade = especialidade
        self.nivel = nivel

    def darAula(self):
        self.__class__.console.print(
            f"O(a) professor(a) {self.nome} acabou de dar aula"
        )

    def estudar(self):
        self.__class__.console.print(
            f"O(a) professor(a) {self.nome} é especialista em {self.especialidade} no {self.nivel}"
        )