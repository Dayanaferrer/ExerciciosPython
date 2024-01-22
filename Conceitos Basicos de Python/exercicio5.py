''' Escreva um programa que calcule o salário líquido.
Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda'''

salario_bruto = float(input('Digite o salário bruto: '))

if salario_bruto <= 1903.98:
  aliquota = 0
elif salario_bruto <= 2826.65:
  aliquota = 7.5
elif salario_bruto <= 3751.05:
  aliquota = 15
elif salario_bruto <= 4664.68:
  aliquota = 22.5
else:
  aliquota = 27.5

imposto = salario_bruto * (aliquota / 100)

salario_liquido = salario_bruto - imposto

print(f'O salário líquido é: R${salario_liquido:.2f}')