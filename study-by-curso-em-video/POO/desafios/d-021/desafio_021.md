# Desafio 021

## Descrição
- Criar uma classe **Caneta**, que simulará o funcionamento de uma **caneta colorida** podendo **escrever** frases na cor relativa.

### Exemplo do código de Instanciamento
```python
c1 = Caneta(
    cor:"azul"
)

c2 = Caneta(
    cor:"vermelha"
)

c3 = Caneta(
    cor:"verde"
)

c2.destampar()
c3.destampar()

c1.escrever(
    mensagem:"Olá, tudo bem? "
)

c1.quebrar_linha(
    quantidade_de_linhas:2
)

c2.escrever(
    mensagem:"Olá, gafanhoto! "
)

c3.escrever(
    mensagem:"Vamos exercitar! "
)
```

### Exemplo da Saída no terminal
:no_entry_sign: A <span style="color:blue">caneta</span> está tampada!
.
<span style="color:red">Olá, gafanhotos!  </span> <span style="color:green"> Vamos exercitar! </span>