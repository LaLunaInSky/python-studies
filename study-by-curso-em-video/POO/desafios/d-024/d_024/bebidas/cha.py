from d_024.bebidas import BebidaQuente

class Cha(BebidaQuente):
    def __init__(self):
        pass

    def misturar(self) -> str:
        return "Mergulhando o sachê de ervas na água."
    
    def servir(self) -> str:
        return "Servindo em uma caneca de porcelana com limão."