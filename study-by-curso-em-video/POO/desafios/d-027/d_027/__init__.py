from d_027.personagens.guerreiro import Guerreiro
from d_027.personagens.mago import Mago

def main():
    personagem_01 = Guerreiro()

    personagem_02 = Mago()

    personagem_01.atacar(
        personagem_02,
        1000
    )

    personagem_02.curar()

    personagem_02.atacar(
        personagem_01,
        20000
    )

    personagem_01.curar()