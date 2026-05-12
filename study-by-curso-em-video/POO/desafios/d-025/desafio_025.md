# Desafio 025

## Descrição
- Crie uma classe capaz de **calcular fretes** de **veículos** diferentes

| Transporte {abstract} |
|-----------------------|
| + distancia |
| + frete |
| + cacularFrete() {abstract} |

| Moto |
|------|
| + valor_do_km = 0.50 |
| + calcularFrete() |

- Frete livre

| Caminhao |
|----------|
| + valor_do_km = 1.20 |
| + calcularFrete() |

- Mínimo 50km de frete

| Drone |
|-------|
| + valor_do_km = 9.50 |
| + calcularFrete() |

- Máximo 10Km

### Exemplo do código de Instanciamento
```python
from rich.console import Console
from transportes import *
from tabela import TabelaDePreco

def main():
    console = Console()

    tabela = TabelaDePreco()

    distancia_1 = 20

    entrega_1 = Moto(
        distancia: distancia_1
    )

    console.print(
        f"Frete de {type(entrega_1).__name__} para {distancia_1}Km = {entrega_1.calcularFrete()}\n"
    )

    entrega_2 = Caminhao(
        distancia: distancia_1
    )

    console.print(
        f"Frete de {type(entrega_2).__name__} para {distancia_1}Km = {entrega_2.calcularFrete()}\n"
    )

    tabela.fretes(
        distancia_1
    )

    distancia_2 = 80

    entrega_3 = Caminhao(
        distancia: distancia_2
    )

    console.print(
        f"Frete de {type(entrega_3).__name__} para {distancia_2}Km = {entrega_3.calcularFrete()}\n"
    )

    entrega_4 = Drone(
        distancia: distancia_2
    )

    console.print(
        f"Frete de {type(entrega_4).__name__} para {distancia_2}Km = {entrega_4.calcularFrete()}\n"
    )

    tabela.fretes(
        distancia_2
    )    

    distancia_3 = 8

    entrega_5 = Drone(
        distancia: distancia_3
    )

    console.print(
        f"Frete de {type(entrega_5).__name__} para {distancia_3}Km = {entrega_5.calcularFrete()}\n"
    )

    tabela.fretes(
        distancia_3
    )    

if __name__ == "__main__":
    main()
```

### Exemplo da Saída no terminal
Frete de Moto para 20Km = R$10.00

Frete de Caminhao para 20Km = Raio mínimo de 50Km

    Tabela de Fretes
| Distância | Tipo | Frete |
|-----------|------|-------|
| 20Km | Moto | R$10.00 |
| 20Km | Caminhao | Raio mínimo de 50Km |
| 20Km | Drone | Raio máximo de 10Km |

Frete de Caminhao para 80Km = R$96.00

Frete de Drone para 80Km = Raio máximo de 10Km

    Tabela de Fretes
| Distância | Tipo | Frete |
|-----------|------|-------|
| 80Km | Moto | R$40.00 |
| 80Km | Caminhao | R$96.00 |
| 80Km | Drone | Raio máximo de 10Km |

Frete de Drone para 8Km = R$76.00

    Tabela de Fretes
| Distância | Tipo | Frete |
|-----------|------|-------|
| 8Km | Moto | R$4.00 |
| 8Km | Caminhao | Raio mínimo de 50Km |
| 8Km | Drone | R$76.00 |