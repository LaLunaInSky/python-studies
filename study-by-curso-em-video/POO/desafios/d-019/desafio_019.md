# Desafio 019

## Descrição
- Criar uma classe **Livro**, onde irá simular a **passagem de páginas** de um livro, considerando também se o usuário **chegou ao final** da leitura.

### Exemplo do código de Instanciamento
```python
l1 = Livro(
    titulo:"10 coisas que aprendi",
    paginas:20
)

l1.avancar_paginas(
    numero_de_paginas:5
)

l1.avancar_paginas(
    numero_de_paginas:10
)

l1.avancar_paginas(
    numero_de_paginas:100
)
```

### Exemplo da Saída no terminal
:open_book: <span style="color:blue">Você acabou de abrir o livro '</span><span style="color:red">10 coisas que aprendi</span><span style="color:blue">' que tem</span> <span style="color:green">20 páginas</span> <span style="color:blue">no total. Você agora está na</span> <span style="color:yellow">página 1</span>

Pág2 ▶ Pág3 ▶ Pág4 ▶ Pág5 ▶ Pág6 ▶ <span style="color:blue">Você avançou 5 páginas e agora está na</span> <span style="color:yellow">página 6</span>

Pág7 ▶ Pág8 ▶ Pág9 ▶ Pág10 ▶ Pág11 ▶ Pág12 ▶ Pág13 ▶ Pág14 ▶ Pág15 ▶ Pág16 ▶ <span style="color:blue">Você avançou 10 páginas e agora está na</span> <span style="color:yellow">página 16</span>

Pág17 ▶ Pág18 ▶ Pág19 ▶ Pág20 ▶  <span style="color:blue">Você avançou 4 páginas e agora está na</span> <span style="color:yellow">página 20</span>
:closed_book: <span style="color:red">Você chegou ao final do livro '10 coisas que aprendi'</span>