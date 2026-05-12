# Desafio 030

## Descrição
- Crie uma classe que gerencie a **hash SHA256** de uma **senha**

| Credencial |
|------------|
| + @senha |
| - __hash |
| + validar(chave) |

### Exemplo do código de Instanciamento 
```python
from solution import Credencial

def main():
    credencial = Credencial()

    credencial.senha = "Gafanhoto"

    credencial.validar(
        chave: "Teste"
    )

    credencial.validar(
        chave: "Gafanhoto"
    )

if __name__ == "__main__":
    main()
```

### Exemplo da Saída no terminal

Senha criada com <span style="background-color:green; color:white; padding:3px; text-transform: uppercase">sucesso!</span>

<span style="background-color:red; color:white; padding:3px; text-transform: uppercase">Senha Incorreta!</span>

<span style="background-color:green; color:white; padding:3px; text-transform: uppercase">Senha Correta!</span>