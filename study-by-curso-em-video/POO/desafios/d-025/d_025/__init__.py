from d_025.transportes.moto import Moto
from d_025.transportes.caminhao import Caminhao
from d_025.transportes.drone import Drone
from d_025.tabela import TabelaDePreco

def main():
    tabela_de_precos = TabelaDePreco()

    distancia_01 = 20

    entrega_01 = Moto(distancia_01)

    entrega_01.analisarFrete()

    entrega_02 = Caminhao(distancia_01)

    entrega_02.analisarFrete()

    tabela_de_precos.fretes(distancia_01)

    distancia_02 = 80

    entrega_03 = Caminhao(distancia_02)

    entrega_03.analisarFrete()

    entrega_04 = Drone(distancia_02)

    entrega_04.analisarFrete()

    tabela_de_precos.fretes(distancia_02)

    distancia_03 = 8

    entrega_05 = Drone(distancia_03)

    entrega_05.analisarFrete()

    tabela_de_precos.fretes(distancia_03)