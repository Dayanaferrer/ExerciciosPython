''' Faça um programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista
 a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0'''

medias = []

for i in range(1, 6):
    print(f"Aluno {i}")
    
    soma = 0
    
    for j in range(1, 5):
        nota = float(input(f"Digite a nota {j}: "))
        soma += nota
    
    media = soma / 4
    
    medias.append(media)

num_alunos = sum(1 for media in medias if media >= 7.0)

print(f"Número de alunos com média maior ou igual a 7.0 foi: {num_alunos}")
