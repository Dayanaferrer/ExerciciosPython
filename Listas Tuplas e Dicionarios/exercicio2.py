''' Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N Noturno. 
Imprima a mensagem "BomDia!", "BoaTarde! "ou" BoaNoite! "ou" ValorInválido!", conforme o caso.'''

turno = input(
    'Digite o turno que você estuda (M-matutino, V-Vespertino, N-Noturno): ')

turno = turno.upper()

if turno == 'M':
  print('Bom dia!')
elif turno == 'V':
  print('Boa Tarde!')
elif turno == 'N':
  print('Boa Noite!')
else:
  print('Opção inválida.')