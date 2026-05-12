from rich.console import Console
from rich.panel import Panel

class Churrasco:
    quantidade_de_carne_por_pessoa = 0.4 #Kg ou 400g
    preco_do_kilo_da_carne = 82.4 #Por cada Kg de carne

    def __init__(
        self,
        titulo: str,
        quantidade_de_pessoas: int
    ):
        self.titulo = titulo
        self.quantidade_de_pessoas = quantidade_de_pessoas


    def calcular_quantidade_total_de_carne(self) -> float:
        quantidade_de_carne_no_total = self.__class__.quantidade_de_carne_por_pessoa * self.quantidade_de_pessoas # Em Kg

        return quantidade_de_carne_no_total
    
    def calcular_custo_total_do_churrasco(self) -> float:
        custo_total_do_churrasco = round(
            self.calcular_quantidade_total_de_carne()
            * 
            self.__class__.preco_do_kilo_da_carne, 
            2
        )

        return custo_total_do_churrasco
    
    def calcular_preco_do_churrasco_para_cada_pessoa(self) -> float:
        preco_do_churrasco_para_cada_pessoa = self.calcular_custo_total_do_churrasco() / self.quantidade_de_pessoas

        return preco_do_churrasco_para_cada_pessoa

    def analisar(self):
        console = Console()

        quantidade_de_carne_no_total = self.calcular_quantidade_total_de_carne()

        custo_total_do_churrasco = self.calcular_custo_total_do_churrasco()

        preco_do_churrasco_para_cada_pessoa = self.calcular_preco_do_churrasco_para_cada_pessoa()

        conteudo_do_panel = f"Analisando [green]{self.titulo}[/] com [blue]{self.quantidade_de_pessoas} convidado{'s' if self.quantidade_de_pessoas != 1 else ''}[/]"

        conteudo_do_panel += f"\nCada participante comerá {self.__class__.quantidade_de_carne_por_pessoa}Kg e cada Kg custa R${self.__class__.preco_do_kilo_da_carne:,.2f}"

        conteudo_do_panel += f"\nRecomendo [blue]comprar {quantidade_de_carne_no_total:.3f}Kg[/] de carne"

        conteudo_do_panel += f"\nO custo total será de [green]R${custo_total_do_churrasco:,.2f}[/]"

        conteudo_do_panel += f"\nCada pessoa pagará [yellow]R${preco_do_churrasco_para_cada_pessoa:,.2f}[/] para participar."

        panel = Panel(
            conteudo_do_panel,
            title=self.titulo,
            expand=False
        )

        console.print(panel)