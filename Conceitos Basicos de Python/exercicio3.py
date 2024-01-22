'''Faça um Programa que peça a quantidade de quilômetros,
 transforme em metros, centímetros e milímetros. '''

quilometros = float(input('Digite a quantidade de quilômetros: '))

metros = quilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10

print(f'{quilometros} quilômetros é igual a {metros} metros.')
print(f'{quilometros} quilômetros é igual a {centimetros} centímetros.')
print(f'{quilometros} quilômetros é igual a {milimetros} milímetros.')
