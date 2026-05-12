from .conta_bancaria import ContaBancaria

def main():
    conta_luiz = ContaBancaria("luiz de melo")
    conta_luiz.visualizarInfoDaConta()

    conta_luiz.depositar(3000)
    conta_luiz.visualizarInfoDaConta()

    conta_luiz.depositar(500)
    conta_luiz.visualizarInfoDaConta()

    conta_luiz.sacar(3499)
    conta_luiz.visualizarInfoDaConta()

    conta_luiz.sacar()
    conta_luiz.visualizarInfoDaConta()