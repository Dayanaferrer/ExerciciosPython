''' Implemente um programa que classifique um aluno com base em sua pontuação em um exame. 
O programa deverá solicitar uma nota de 0 a 10. Se apontuação for maior ou igual a 7,
o aluno é aprovado; caso contrário, é reprovado'''

nota = -1

while nota < 0 or nota > 10:
    nota = float(input('Insira sua nota do exame:'))

if nota >= 7:
    print(f'Aprovado Nota: {nota}')
else:
     print(f'Reprovado Nota: {nota}')