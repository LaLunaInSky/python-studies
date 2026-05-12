from rich.console import Console
from rich.panel import Panel
from subprocess import run

class ControleRemoto:
    console = Console()
    canal_min: int = 1
    canal_max: int = 5
    volume_min: int = 0
    volume_max: int = 5
    
    def __init__(self):
        self.tv_ligada = True
        self.canal = self.__class__.canal_min
        self.volume = 2

    def mostradorDaTv(self) -> str:
        mensagem_canal = "Canal  = "

        for canal in range(
            self.__class__.canal_min, 
            self.__class__.canal_max + 1
        ):
            if self.canal == canal:
                mensagem_canal += f"[yellow on yellow] {canal} [/]"
            else:
                mensagem_canal += f" {canal} "

        mensagem_final = mensagem_canal

        mensagem_volume = "\nVolume = "

        for volume in range(
            self.__class__.volume_min, 
            self.volume
        ):
            mensagem_volume += f"[on cyan]{" "*3}[/]"

        for volume in range(
            self.volume + 1, 
            self.__class__.volume_max + 1
        ):
            mensagem_volume += f"[on bright_black]{" "*3}[/]"
            
            

        mensagem_final += mensagem_volume

        return mensagem_final

    def mudarDeCanal(
        self,
        seta: str
    ) -> str:
        match seta:
            case '<':
                if self.canal == self.__class__.canal_min:
                    self.canal = self.__class__.canal_max
                else:
                    self.canal -= 1
                
                return self.mostradorDaTv()
            case '>':
                if self.canal == self.__class__.canal_max:
                    self.canal = self.__class__.canal_min
                else:
                    self.canal += 1

                return self.mostradorDaTv()
            case _:
                return ""

    def mudarOVolume(
        self,
        sinal: str
    ) -> str:
        match sinal:
            case '+':
                if self.volume != self.__class__.volume_max:
                    self.volume += 1

                return self.mostradorDaTv()
            case '-':
                if self.volume != self.__class__.volume_min:
                    self.volume -= 1

                return self.mostradorDaTv()
            case _:
                return ""

    def verificarSeATvEstaLigadaOuDesligada(
        self,
        botao_apertado: str = ''
    ) -> str:
        match botao_apertado:
            case "@":
                if self.tv_ligada:
                    self.tv_ligada = False

                    return ":no_entry_sign: [red]A TV está desligada [/]"
                else:
                    self.tv_ligada = True
                    self.canal = self.__class__.canal_min
                    self.volume = 2

                    return self.mostradorDaTv()
            case _:
                if not self.tv_ligada:
                    return ":no_entry_sign: [red]A TV está desligada [/]"
                else:
                    match botao_apertado:
                        case '<' | '>':
                            return self.mudarDeCanal(botao_apertado)
                        case '-' | '+':
                            return self.mudarOVolume(botao_apertado)
                        case _:
                            return self.mostradorDaTv()

    def sistemaDaTv(self):
        input_user = '@'
        
        while input_user != '0':
            run("clear", shell=False)
            
            conteudo_do_panel = self.verificarSeATvEstaLigadaOuDesligada(input_user)
            
            panel = Panel(
                conteudo_do_panel,
                title="[TV]",
                expand=False
            )

            self.__class__.console.print(panel)

            input_user = str(input(f"< CH{self.canal} >  - VOL{self.volume} + "))

