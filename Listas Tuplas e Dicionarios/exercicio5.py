''' Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de 
um triângulo e classifique-o como equilátero, isósceles ou escaleno.
            Equilátero: todos os lados com o mesmo valor.
            Isósceles: dois lados como mesmo valor 
            Escaleno: todos os lados com medidas distintas'''

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")