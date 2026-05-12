from random import randint
from rich.console import Console

class ContaBancaria:
    __console = Console()

    __error_value_negative = ValueError("Não é possivel entrar com um valor negativo")

    def __init__(
        self, 
        nome_do_titular
    ):
        self.__numero_da_conta = randint(1, 5000)
        self.__titular = nome_do_titular
        self.__saldo = 0.0

        self.__class__.__console.print(f"\nOlá {self.__titular.title()} sua conta de número {self.__numero_da_conta} foi criada com sucesso.")
    
    def sacar(
        self,
        valor_do_saque: float = 2.0
    ):
        if valor_do_saque <= self.__saldo:
            if valor_do_saque >= 2.0:
                self.__saldo -= valor_do_saque

                self.__class__.__console.print(f"\n{self.__titular.title()} o saque de R${valor_do_saque:,.2f} foi realizado com sucesso.")
            else:
                raise self.__class__.__error_value_negative
        else:
            self.__class__.__console.print(f"\n{self.__titular.title()} não possui saldo suficiente para o saque no valor de R${valor_do_saque:,.2f}.")

    def depositar(
        self,
        valor_do_deposito = 1.0
    ):
        if valor_do_deposito >=  1.0:
            
            self.__saldo += valor_do_deposito

            self.__class__.__console.print(f"\n{self.__titular.title()} o depósito de R${valor_do_deposito:,.2f} foi realizado com sucesso.")
        else:
            raise self.__class__.__error_value_negative

    def visualizarInfoDaConta(self):
        self.__class__.__console.print(
            f"\nA conta de número '{self.__numero_da_conta}' do titular '{self.__titular.title()}' possui o saldo de R${self.__saldo:,.2f}."
        )