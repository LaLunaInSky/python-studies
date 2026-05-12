from rich.console import Console

class Caneta:
    console = Console()

    def __init__(
        self,
        cor: str
    ):
        self.cor_caneta = ""

        self.caneta_tampada = True

        match cor:
            case "vermelha":
                self.cor_caneta = "red"
            case "verde":
                self.cor_caneta = "green"
            case "azul":
                self.cor_caneta = "blue"
            case _:
                self.__class__.console.print(f"A cor '{cor}' não existe, tente a 'vermelha', 'azul' ou 'verde'!")

                self.cor_caneta = ""

    
    def destampar(self):
        self.caneta_tampada = False

    def tampar(self):
        self.caneta_tampada = True

    def escrever(
        self,
        mensagem: str
    ):
        if self.caneta_tampada:
            self.__class__.console.print(
                f":no_entry_sign: A [{self.cor_caneta}]caneta[/] está tampada!"
            )
        else:
            self.__class__.console.print(
                f"[{self.cor_caneta}]{mensagem}[/]",
                end=""
            )

    def quebrar_linha(
        self,
        quantidada_de_linhas: int = 1
    ):
        for linha in range(0, quantidada_de_linhas):
            self.__class__.console.print()