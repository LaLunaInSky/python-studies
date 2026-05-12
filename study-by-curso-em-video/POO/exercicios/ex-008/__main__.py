from avaliacao import Avaliacao

def main():
    avaliacao_01 = Avaliacao(
        "Pedro",
        "Matemática"
    )

    avaliacao_01.nota_do_aluno = 8.75

    print(avaliacao_01.nota_do_aluno)

    avaliacao_01.verDadosDoAluno()

if __name__ == "__main__":
    main()