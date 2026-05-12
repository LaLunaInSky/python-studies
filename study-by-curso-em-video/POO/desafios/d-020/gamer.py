from rich.console import Console
from rich.panel import Panel

class Gamer: 

    def __init__(
        self,
        nome: str,
        nick: str
    ):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favoritos(
        self,
        jogo: str
    ):
        self.jogos.append(jogo)

    def verificar_se_possue_jogos(self) -> bool:
        return True if self.jogos.__len__() > 0 else False

    def ficha(self):
        console = Console()

        title_do_panel = f"Jogador <{self.nick}>"

        conteudo_do_panel = f"Nome real: [white on blue] {self.nome} [/]\n"

        conteudo_do_panel += "Jogos Favoritos:"

        if self.verificar_se_possue_jogos():
            for jogo in sorted(self.jogos):
                conteudo_do_panel += f"\n:video_game: [blue]{jogo}[/]"
        else:
            conteudo_do_panel += "\n[red]Nenhum jogo adicionado[/]"

        panel = Panel(
            conteudo_do_panel,
            expand=False,
            title=title_do_panel
        )

        console.print(panel)