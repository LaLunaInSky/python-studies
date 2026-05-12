# Desafio 023

## Descrição
- Implemente o seguinte **diagrama de classes**:

| Poligno {abstract} |
|--------------------|
| + qtd_lados |
| + perimetro() {abstract} |
| + area() {abstract} |

| Quadrado |
|----------|
| + comprimento_lado |
| + perimetro() |
| + area() |

| Circulo |
|---------|
| + raio |
| + perimetro() |
| + area() 

### Exemplo do código de Instanciamento
```python
from rich.console import Console
from poligonos import *

def main():
    console = Console()

    p1 = Quadrado(
        comprimento_lado: 12
    )

    console.print(
        "Dados do Quadrado"
    )

    console.print(
        f"Perímetro = {p1.perimetro():.1f}"
    )

    console.print(
        f"Area = {p1.area():.1f}"
    )

    p2 = Circulo(
        raio: 20
    )

    console.print(
        f"\nDados do Circulo"
    )

    console.print(
        f"Perímetro = {p2.perimetro():.1f}"
    )

    console.print(
        f"Area = {p2.area():.1f}"
    )

if __name__ = "__main__":
    main()
```

### Exemplo da Saída no terminal
```console
Dados do Quadrado
Perímetro = 48.0
Area = 144.0

Dados do Circulo
Perímetro = 125.7
Area = 1256.6
```