#Faça um programa que peça dois números e imprima o maior deles.

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

if x > y:
  print(f'O número maior é {x}.')
elif y > x:
  print(f'O número maior é {y}.')
else:
  print('Os números são iguais.')