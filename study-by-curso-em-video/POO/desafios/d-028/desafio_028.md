# Desafio 028

## Descrição
- Implemente um **termostato** orientado a objeto:
    * Mínima: **16°C**
    * Máxima: **30°C**
    * Incremento: **0.5°C**
    * Temperatura Inicial: **24°C**

| Termostato |
|------------|
| - __temperatura |
| + @temperatura |
| + @temperaturaFormatada |

### Exemplo do código de Instanciamento
```python
from solution import Termostato

def main():
    termostato = Termostato()

    termostato.temperatura = 20

    termostato.temperatura = 12

    termostato.temperatura = 40

    termostato.temeratura = 25.5

    termostato.temperatura = 25.2


if __name__ == "__main__":
    main()
```

### Exemplo da Saída no terminal

<span style="color:blue">Termostato</span> ligado em <span style="color:red">24°C</span>

<span style="color:blue">Termostato</span> ajustado para <span style="color:red">20°C</span>

<span style="color:blue">Termostato</span> ajustado para <span style="color:red">16°C</span>

<span style="color:blue">Termostato</span> ajustado para <span style="color:red">30°C</span>

<span style="color:blue">Termostato</span> ajustado para <span style="color:red">25.5°C</span>

<span style="color:purple">ValueError: Temperatura de 25.2°C é inválida!</span>