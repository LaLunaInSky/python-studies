from d_027.personagens import Personagem
from rich.console import Console
from random import randrange

class Mago(Personagem):
    def __init__(
        self,
        nome: str = "Merlin",
        quantidade_de_vida: int = 3000,
    ):
        golpes = [
            "Bola de Fogo",
            "Raio de Luz",
            "Magia Estática"
        ]

        super().__init__(
            nome,
            quantidade_de_vida,
            golpes
        )

    def curar(self):
        console = Console()

        if self.quantidade_de_vida <= 0:
            console.print(
                f"[blue]{self.nome}[/] está [red]morto[/], e não pode recuperar vida!"
            )

        else:
            quantidade_de_vida_recuperada = randrange(
                0,
                100
            )

            self.quantidade_de_vida += quantidade_de_vida_recuperada

            console.print(
                f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {quantidade_de_vida_recuperada} pontos[/] de vida.\n"
            )
