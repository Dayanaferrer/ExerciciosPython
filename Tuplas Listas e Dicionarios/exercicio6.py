''' Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário 
de trás para frente utilizando somente letras maiúsculas. 
Dica:lembre-se que ao informar o nome ou suário pode digitar letras maiúsculas ou minúsculas.'''

nome = input("Digite o seu nome: ")

nome_invertido = nome.upper()[::-1]

print(nome_invertido)
