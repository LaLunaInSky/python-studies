from rich import inspect
from exercise.pessoas.aluno import Aluno
from exercise.pessoas.professor import Professor
from exercise.pessoas.funcionario import Funcionario

def main():
    aluno_01 = Aluno(
        "José",
        17,
        "Informática",
        "T01"
    )

    aluno_01.fazerAniversario()
    aluno_01.fazerMatricula()

    inspect(aluno_01, methods=True)

    professor_01 = Professor(
        "Samuel",
        37,
        "Biologia",
        "Mestrado"
    )

    professor_01.fazerAniversario()
    professor_01.darAula()

    inspect(professor_01, methods=True)

    funcionario_01 = Funcionario(
        "Cláudia",
        27,
        "Secretária",
        "Secrataria"
    )

    funcionario_01.fazerAniversario()
    funcionario_01.baterPonto()

    inspect(funcionario_01, methods=True)