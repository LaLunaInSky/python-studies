from d_026.funcionarios import Funcionario

class FuncionarioHorista(Funcionario):
    def __init__(
        self,
        nome: str = "Fulano",
        valor_da_hora: float = 9.60,
        horas_trabalhadas: int = 220
    ):
        self.valor_da_hora = valor_da_hora
        self.horas_trabalhadas = horas_trabalhadas

        super().__init__(
            nome,
            valor_da_hora * horas_trabalhadas
        )

    def calcularSalario(self):
        salario_desconto = (
            self.__class__.inss / 100
        ) * self.salario_bruto

        self.salario = self.salario_bruto - salario_desconto