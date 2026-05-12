class Pessoa:
    def __init__(
        self,
        nome: str,
        idade: int
    ):
        self.nome = nome
        self.idade = idade

    def fazerAniversario(self):
        self.idade += 1