''' Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.'''

ganho_por_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = float(input('Digite o número de horas trabalhadas no mês: '))

salario_total = ganho_por_hora * horas_trabalhadas

print(f'O total do seu salário neste mês é: R$ {salario_total:.2f}')