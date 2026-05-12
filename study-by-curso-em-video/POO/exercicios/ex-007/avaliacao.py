from rich.console import Console
from rich.panel import Panel

class Avaliacao:
    def __init__(
        self,
        nome_do_aluno: str,
        disciplina: str
    ):
        self.nome_do_aluno = nome_do_aluno
        self.disciplina = disciplina
        self._nota_do_aluno_na_disciplina = 0.0

    def getNotaDoAluno(self) -> float:
        return self._nota_do_aluno_na_disciplina

    def setNotaDoAluno(
        self,
        nota: float = 0.0
    ):
        error_nota = ValueError(f"Nota {nota} inválida, porfavor inserir de 0.0 á 10.0")

        if nota >= 0.0 and nota <= 10.0:
            self._nota_do_aluno_na_disciplina = round(nota, 1)
        else:
            raise error_nota


    def verDadosDoAluno(self):
        console = Console()

        conteudo_do_panel = f"Nome: [blue]{self.nome_do_aluno}[/]\nDisciplina: [blue]{self.disciplina}[/]\nNota: [blue]{self._nota_do_aluno_na_disciplina:.1f}[/]"

        panel = Panel(
            conteudo_do_panel,
            title="Aluno",
            expand=False
        )

        console.print(panel)