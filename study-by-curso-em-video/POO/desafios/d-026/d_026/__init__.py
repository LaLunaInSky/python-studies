from d_026.funcionarios.horista import FuncionarioHorista
from d_026.funcionarios.mensalista import FuncionarioMensalista

def main():
    funcionario_01 = FuncionarioHorista(
        "Paulo",
        12,
        200
    )

    funcionario_01.calcularSalario()
    funcionario_01.analisarSalario()

    funcionario_02 = FuncionarioMensalista(
        "Amanda",
        9500
    )

    funcionario_02.calcularSalario()
    funcionario_02.analisarSalario()