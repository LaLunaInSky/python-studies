from d_024.bebidas import BebidaQuente

class Cafe(BebidaQuente):
    def __init__(self):
        pass

    def misturar(self) -> str:
        return f"Passando a água pressurizada pelo pó de café moido."
    
    def servir(self) -> str:
        return f"Servindo uma xícara pequena."