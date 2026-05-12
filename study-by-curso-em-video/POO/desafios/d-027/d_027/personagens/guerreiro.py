from d_027.personagens import Personagem
from rich.console import Console
from random import randrange

class Guerreiro(Personagem):
    def __init__(
        self,
        nome: str = "Kratos",
        quantidade_de_vida: int = 2000
    ):
        golpes = [
            "Soco",
            "Golpe de Machado",
            "Pulo Giratório"
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
                f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {quantidade_de_vida_recuperada} pontos[/] de vida.\n"
            )