from exercise.pessoas import Pessoa

from rich.console import Console

class Aluno(Pessoa):
    def __init__(
        self,
        nome: str,
        idade: int,
        curso: str,
        turma: str
    ):
        super().__init__(
            nome,
            idade
        )
        
        self.curso = curso
        self.turma = turma

    def fazerMatricula(self):
        console = Console()

        console.print(
            f"O(a) aluno(a) {self.nome} acabou de fazer a matrícula"
        )