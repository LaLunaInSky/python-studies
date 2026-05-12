from exercise.pessoas import Pessoa

from rich.console import Console

class Professor(Pessoa):
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
        console = Console()

        console.print(
            f"O(a) professor(a) {self.nome} acabou de dar aula"
        )