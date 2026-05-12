from d_024.bebidas import BebidaQuente

class Leite(BebidaQuente):
    def __init__(self):
        pass

    def misturar(self) -> str:
        return "Passando o vapor pressurizado pelo bico do leite."
    
    def servir(self) -> str:
        return "Servindo em uma caneca grande, já com café."