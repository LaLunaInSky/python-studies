# Desafio 024

## Descrição
- Simule uma **cafeteira** orientada a objetos

| BebidaQuente {abstract} |
|-------------------------|
| + preparar() |
| + ferverAgua() |
| + misturar() {abstract} |
| + servir() {abstract} |

| Cafe |
|------|
| + misturar() |
| + servir() |

| Cha |
|-----|
| + misturar() |
| + servir() |

| Leite |
|-------|
| + misturar() |
| + servir() |

### Exemplo do código de Instanciamento
```python
from cafeteria import *

def main():
    bebida_1 = Cafe()
    bebida_1.preparar()

    bebida_2 = Cha()
    bebida_2.prepara()

    bebida_3 = Leite()
    bebida_3.prepara()

if __name__ == "__main__":
    main()
```

### Exemplo da Saída no terminal
```console
--- Iniciando o Preparo do Café ---
1. Fervendo a água a 100 graus Celsius.
2. Passando água pressurizada pelo pó de café moido.
3. Servindo uma xícara pequena.
--- Bebida Pronta ---

--- Iniciando o Preparo do Chá ---
1. Fervendo a água a 100 graus Celsius.
2. Mergulhando o sachê de ervas na água.
3. Servindo na caneca de porcelana com limão
--- Bebida Pronta ---

--- Iniciando o Preparo do Leite ---
1. Fervendo a água a 100 graus Celsius.
2. Passando vapor pressurizado pelo bico do leite.
3. Servindo na caneca grande, já com café.
--- Bebida Pronta ---
```