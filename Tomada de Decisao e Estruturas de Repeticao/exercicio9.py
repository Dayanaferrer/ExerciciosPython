''' O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos.
O processo de leitura deve ser encerrado quando o usuário informar o valor zero. 
Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos. '''

contagem_pares = 0
contagem_impares = 0

while True:
    num = float(input("Digite um número (ou 0 para sair): "))
    if num == 0:
        break
    elif num < 0:
        print("Por favor, insira apenas números positivos.")
        continue

    elif num % 2 == 0:
        contagem_pares += 1
    else:
        contagem_impares += 1

print(f"Você inseriu {contagem_pares} números pares e {contagem_impares} números ímpares.")