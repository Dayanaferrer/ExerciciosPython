''' Reverso do número. Faça uma função que retorne o reverso de um 
número inteiro informado. Por exemplo: 127 -> 721'''

def reverso_numero(num):
    return int(str(num)[::-1])

num = int(input("Por favor, insira um número: "))
resultado = reverso_numero(num)

print(f'O numero digitado: {num} e seu reverso é = {resultado}')