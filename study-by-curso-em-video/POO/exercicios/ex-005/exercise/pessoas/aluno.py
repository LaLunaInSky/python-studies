from exercise.pessoas import Pessoa
from rich.console import Console

class Aluno(Pessoa):
    console = Console()

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
        self.__class__.console.print(
            f"O(a) aluno(a) {self.nome} acabou de fazer a matrícula"
        )

    def estudar(self):
        self.__class__.console.print(
            f"O(a) aluno(a) {self.nome} está estudando {self.curso} na turma {self.turma}"
        )