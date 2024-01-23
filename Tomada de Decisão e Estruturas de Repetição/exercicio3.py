''' Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o 
valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota >= 0 and nota <= 10:
        print(f'Nota válida! Você escolheu {nota}')
        break
    else:
        print('Nota inválida! Por favor, digite uma nota entre 0 e 10.')