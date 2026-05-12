# Desafio 018

## Descrição
- Criar uma classe **Churrasco**, onde poderemos informar a **quantidade de pessoas** que iram participar, a **quantidade de carne** que precisará ser comprada, o **custo total** do churrasco, e o **custo por pessoa**.

### Exemplo do código de Instanciamento
```python
c1 = Churrasco(
    titulo:"Churras dos Amigos",
    quantidade_de_pessoas:15
)

c1.analisar()

# CONSIDERE:
# Consumo padrão: 400g por pessoa
# Preço da carne: R$ 82,40/Kg
```

### Exemplo da Saída no terminal
| Churras dos Amigos |
|----------------|
| Analisando <span style="color:green">Churras dos Amigos</span> com <span style="color:blue">15 convidados</span> |
| Cada participante comerá 0.4Kg e cada KG custa RS82.40 |
| Recomendo comprar 6.000Kg de carne |
| O custo total será de <span style="color:green"> RS494.40 </span> |
| Cada pessoa pagará <span style="color:yellow">RS32.96</span> para participar. |