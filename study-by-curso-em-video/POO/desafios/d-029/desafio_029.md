# Desafio 029

## Descrição
- Simule um **diário secreto** orientado a objeto:
    * Senha Padrão: CeV!@

| Diario |
|--------|
| - __segredos[str] |
| - __senha |
| + escrever(mensagem) |
| + ler(senha) |

### Exemplo do código de Instanciamento
```python
from solution import Diario

def main():
    diario = Diario(
        nova_senha: "Gafanhoto"
    )

    diario.escrever(
        mensagem: "Primeira Mensagem"    
    )

    diario.escrever(
        mensagem: "Você é uma pessoa simpática"
    )

    diario.escrever(
        mensagem: "Você gosta de Python"
    )

    diario.ler()

    diario.ler(
        senha: "Gafanhoto"
    )

if __name__ == "__main__":
    main()
```

### Exemplo da Saída no terminal

Diário criado com <span style="background-color:green; color:white; padding:3px; text-transform: uppercase">sucesso!</span>

Mensagem escrita com <span style="background-color:green; color:white; padding:3px; text-transform: uppercase">sucesso!</span>

Mensagem escrita com <span style="background-color:green; color:white; padding:3px; text-transform: uppercase">sucesso!</span>

Mensagem escrita com <span style="background-color:green; color:white; padding:3px; text-transform: uppercase">sucesso!</span>

<span style="background-color:red; color:white; padding:3px; text-transform: uppercase">Não foi possivel ler o Diário pois esta não é a senha</span>

</br><span style="background-color:green; color:white; padding:3px; text-transform: uppercase">Diário Liberado!<span>
- Primeira Mensagem
- Você é uma pessoa simpática
- Você gosta de Python