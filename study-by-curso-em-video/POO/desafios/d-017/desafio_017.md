# Desafio 017

## Descrição
- Criar uma classe **Produto**, onde poderemos cadastrar o **nome** e o **preco**.
- Crie também um método que mostre uma **etiqueta** do preço do produto.

### Exemplo do códgio de Instanciamento
```python
p1 = Produto(
    nome:"iPhone 17 Pro Max",
    preco:25000.85
)

p2 = Produto(
    nome:"Notebook Gamer",
    preco:8000
)

p1.etiqueta()
p2.etiqueta()
```

### Exemplo da Saída no terminal
| Produto |
|---------|
| Iphone 17 Pro Max |
| R$ 25,000.85 |

| Produto |
|---------|
| Nootebook Gamer |
| R$ 8,000.00 |