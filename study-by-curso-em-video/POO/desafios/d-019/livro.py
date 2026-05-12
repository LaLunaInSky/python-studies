from rich.console import Console
from time import sleep

class Livro:
    def __init__(
        self,
        titulo: str,
        paginas: int    
    ):
        self.titulo = titulo
        self.total_de_paginas = paginas
        self.pagina_atual = 1

        console = Console()

        console.print(
            f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/red]' que tem [green]{self.total_de_paginas} páginas[/green] no total. Você agora está na [yellow]página {self.pagina_atual}[/]\n"
        )

    def verificar_se_esta_na_ultima_pagina(self) -> bool:
        return self.pagina_atual == self.total_de_paginas

    def avancar_paginas(
        self,
        numero_de_paginas: int = 1
    ):
        total_de_páginas_avançadas = 0

        console = Console()

        for pagina in range(
            self.pagina_atual + 1,
            self.pagina_atual + 1 + numero_de_paginas
        ):
            if not self.verificar_se_esta_na_ultima_pagina():
                self.pagina_atual += 1

                total_de_páginas_avançadas += 1

                console.print(
                    f"Pág{pagina} :arrow_forward:", end=" "
                )

                sleep(0.3)
        
        console.print(
            f"[blue]Você avançou {total_de_páginas_avançadas} páginas e agora está na [yellow]página {self.pagina_atual}[/]"
        )

        if self.verificar_se_esta_na_ultima_pagina():
            sleep(0.5)

            console.print(
                f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]"
            )

        console.print()

        sleep(1)