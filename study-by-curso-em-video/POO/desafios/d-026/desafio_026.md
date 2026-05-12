# Desafio 026

## Descrição 
- Crie uma estrutura capaz de **calcular salários** de **funcionários** diferentes:

| Funcionario {abstract} |
|------------------------|
| + nome |
| + salario_bruto |
| + salario |
| + salario_minimo = 1612.00 |
| + inss = 7.5 |
| + calcularSalario() {abstract} |
| + analisarSalario() |

| Horista |
|---------|
| + valor_da_hora |
| + horas_trabalhadas |
| + calcularSalario() |

| Mensalista |
|------------|
| + calcularSalario() |

### Exemplo do código de Instanciamento
```python
from funcionarios import *

def main():
    f1 = FuncionarioHorista(
        nome: "Paulo",
        valor_da_hora: 12,
        horas_trabalhadas: 200
    )

    f1.calcularSalario()
    f1.analisarSalario()

    f2 = FuncionarioMensalista(
        nome: "Amanda",
        salario_bruto: 9500
    )

    f2.calcularSalario()
    f2.analisarSalario()

if __name__ == "__main__":
    main()
```

### Exemplo da Saída no terminal
| Análise de Salário |
|--------------------|
| O salário de <span style="color:blue">Paulo</span> (<span style="color:purple">FuncionarioHorista</span>) é de |
| R$2220.00 e corresponde a <span style="color:yellow">1.4 salários</span> |
| <span style="color:yellow">mínimos</span>. |

| Análise de Salário |
|--------------------|
| O salário de <span style="color:blue">Amanda</span> (<span style="color:purple">FuncionarioMensalista</span>) é |
| de R$8787.00 e corresponde a <span style="color:yellow">5.5 salários</span> |
| <span style="color:yellow">mínimos</span>. |