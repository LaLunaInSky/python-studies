from abc import ABC, abstractmethod
from rich.console import Console
from random import randrange, choice

class Personagem(ABC):
    def __init__(
        self,
        nome: str,
        quantidade_de_vida: int,
        golpes: list[str]
    ):
        self.nome = nome
        self.quantidade_de_vida = quantidade_de_vida
        self.golpes = golpes

    def receberDano(
        self,
        dano_recebido: int
    ):
        console = Console()

        if self.quantidade_de_vida <= 0:
            self.quantidade_de_vida = 0
            
            console.print(
                f"[blue]{self.nome}[/] [red]não possue vida[/]!\n"
            )

        else:
            if self.quantidade_de_vida <= 0:
                self.quantidade_de_vida = 0

            else:
                self.quantidade_de_vida -= dano_recebido

            console.print(
                f"[blue]{self.nome}[/] recebeu [red]dano de {dano_recebido}[/]!\n"
            )


    def atacar(
        self,
        alvo_do_ataque: Personagem,
        forca_do_ataque: int = 100
    ):
        console = Console()

        if self.quantidade_de_vida <= 0:
            console.print(
                f"[blue]{self.nome}[/] está [red]morto[/] para poder atacar."
            )

        else:
            console.print(
                f"[green]{self.nome}[/]([cyan]{self.quantidade_de_vida}[/]) atacou [red]{alvo_do_ataque.nome}[/]([cyan]{alvo_do_ataque.quantidade_de_vida}[/]) com um [blue]{choice(self.golpes)}[/] de força [cyan]{forca_do_ataque}[/]"
            )

            dano_dado = randrange(
                0,
                forca_do_ataque + 1
            )

            alvo_do_ataque.receberDano(
                dano_dado
            )

        @abstractmethod
        def curar(self):
            pass