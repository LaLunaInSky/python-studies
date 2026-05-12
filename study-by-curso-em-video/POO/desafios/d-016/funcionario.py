from rich.console import Console

class Funcionario:
    # Atributos de Classe
    empresa = "Curso em Vídeo"

    def __init__(
        self,
        nome: str,
        setor: str,
        cargo: str
    ):
        # Atributos de Instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        console = Console()
        
        console.print(f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}.")