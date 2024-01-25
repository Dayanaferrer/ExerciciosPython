''' Crie uma função chamada contar_vogais que recebe uma string como parâmetro.
Implemente a lógica para contar o número de vogais na string e retorne o total de vogais.
Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.'''

def contar_vogais(texto):
    vogais = 'aeiou'
    return sum(1 for char in texto.lower() if char in vogais)

frase = input("Insira uma frase: ")

total_vogais = contar_vogais(frase)
print(f'A frase contém {total_vogais} vogais.')