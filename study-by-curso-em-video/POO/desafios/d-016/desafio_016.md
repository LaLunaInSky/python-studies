# Desafio 016

## Descrição
- Criar uma classe **Funcionario**, onde poderemos cadastrar **nome**, **setor** e **cargo**.
- Crie também um método que permita o funcionário se apresentar.

### Exemplo do código de Instanciamento
```python
c1 = Funcionario(
    nome:"Maria", 
    setor:"Administração", 
    cargo:"Diretoria"
)

print(c1.apresentacao())

c2 = Funcionario(
    nome:"Pedro", 
    setor:"TI", 
    cargo:"Programador"
)

print(c2.apresentacao())
```

### Exemplo da Saída no terminal

:handshake: Olá, sou <span style="color:blue">Maria</span> e sou Diretora do setor de Administração da empresa Curso em Vídeo.

:handshake: Olá, sou <span style="color:blue">Pedro</span> e sou Programador do setor de TI da empresa Curso em Vídeo.