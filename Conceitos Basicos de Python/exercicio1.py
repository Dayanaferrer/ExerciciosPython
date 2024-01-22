''' Faça um Programa que peça dois números, realize as 
principais operações soma, subtração, multiplicação, divisão. '''


def menu():
  print("""
  =============== MENU ===============

  1 - Soma
  2 - Subtração
  3 - Multiplicação
  4 - Divisão
  0 - Sair

 ====================================  
  """)

def calc_soma(a, b):
  return a + b


def calc_subtracao(a, b):
  return a - b


def calc_multiplicacao(a, b):
  return a * b


def calc_divisao(a, b):
  if b != 0:
    return a / b
  else:
    print("Erro: Divisão por zero.")
    return None

while True:
  menu()

  opcao = int(input('Escolha uma opção: '))

  if opcao == 0:
    print("Beijos de bytes! Até logo, programadora!")
    break
  elif opcao in [1, 2, 3, 4]:
    a = int(input('Digite o primeiro numero: '))
    b = int(input('Digite o segundo numero: '))

    if opcao == 1:
      print(f'O resultado da Soma é = {calc_soma(a, b)}')
    elif opcao == 2:
      print(f'O resultado da Subtração é = {calc_subtracao(a, b)}')
    elif opcao == 3:
      print(f'O resultado da Multiplicação é = {calc_multiplicacao(a, b)}')
    elif opcao == 4:
      resultado = calc_divisao(a, b)
      if resultado is not None:
        print(f'O resultado da Divisão é = {resultado}')
  else:
    print("Opção inválida. Tente novamente.")