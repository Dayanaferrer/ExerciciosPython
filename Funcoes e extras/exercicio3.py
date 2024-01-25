''' Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. 
Para cada opção, crie uma função. Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, 
onde esse menu chama a função de conversão correta.'''

def celsius_para_fahrenheit(temp_celsius):
    return temp_celsius * 9/5 + 32

def fahrenheit_para_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9

def menu():
    print("1. Converter Celsius para Fahrenheit")
    print("2. Converter Fahrenheit para Celsius")
    escolha = int(input("Escolha uma opção (1 ou 2): "))
    if escolha == 1:
        temp_celsius = float(input("Insira a temperatura em Celsius: "))
        print("Temperatura em Fahrenheit: ", celsius_para_fahrenheit(temp_celsius))
    elif escolha == 2:
        temp_fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))
        print("Temperatura em Celsius: ", fahrenheit_para_celsius(temp_fahrenheit))
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

menu()
