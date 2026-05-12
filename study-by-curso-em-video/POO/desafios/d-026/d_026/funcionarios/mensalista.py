from d_026.funcionarios import Funcionario

class FuncionarioMensalista(Funcionario):
    def __init__(
        self,
        nome: str = "Fulano",
        salario_bruto: float = 1621.0
    ):
        super().__init__(
            nome,
            salario_bruto
        )

    def calcularSalario(self):
        salario_desconto = (
            self.__class__.inss / 100    
        ) * self.salario_bruto

        self.salario = self.salario_bruto - salario_desconto