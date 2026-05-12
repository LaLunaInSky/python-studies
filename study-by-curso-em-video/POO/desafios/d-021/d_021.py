from caneta import Caneta

caneta_azul = Caneta("azul")

caneta_vermelha = Caneta("vermelha")

caneta_verde = Caneta("verde")

caneta_azul.destampar()
caneta_vermelha.destampar()
caneta_verde.destampar()

caneta_azul.escrever(
    "Olá, tudo bem? "
)

caneta_azul.quebrar_linha(2)

caneta_vermelha.escrever(
    "Olá, gafanhoto! "
)

caneta_verde.escrever(
    "Vamos exercitar! "
)

caneta_verde.quebrar_linha()