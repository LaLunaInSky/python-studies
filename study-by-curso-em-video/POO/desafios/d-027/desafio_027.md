# Desafio 027

## Descrição
- Simule o sistema de **batalha** entre **personagens** de um **RPG**:

| Personagem {abstract} |
|-----------------------|
| + nome |
| + vida |
| + golpes |
| + atacar(alvo, forca) |
| + receberDano(dano) |
| + curar() {abstract} |

| Guerreiro |
|-----------|
| + curar() |

| Mago |
|------|
| + curar() |

### Exemplo do código de Instanciamento
```python
from personagens import *

def main():
    p1 = Guerreiro(
        nome: "Kratos",
        vida: 2000
    )

    p2 = Mago(
        nome: "Merlin",
        vida: 3000
    )   

    p1.atacar(
        p2,
        forca: 1000
    )

    p2.curar()

    p2.atacar(
        p1,
        forca: 20000
    )

    p1.curar()

if __name__ == "__main__":
    main()
```

### Exemplo da Saída no terminal

<span style="color:green">Kratos</span>(<span style="color:cyan">2000</span>) atacou <span style="color:red">Merlin</span>(<span style="color:cyan">3000</span>) com um <span style="color:blue">Soco</span> de força <span style="color:cyan">1000</span>
<span style="color:blue">Merlin</span> recebeu <span style="color:red">dano de 602</span>!
<span style="color:blue">Merlin</span> fez uma magia de cura e <span style="color:green">recuperou 56 pontos</span> de vida.

<span style="color:green">Merlin</span>(<span style="color:cyan">2398</span>) atacou <span style="color:red">Kratos</span>(<span style="color:cyan">2000</span>) com um <span style="color:blue">Bola de Fogo</span> de força <span style="color:cyan">20000</span>
<span style="color:blue">Kratos</span> recebeu <span style="color:red">dano de 13455</span>!
<span style="color:blue">Kratos</span> enrolou uma atadura nos ferimentos e <span style="color:green">recuperou 5 pontos</span> de vida.