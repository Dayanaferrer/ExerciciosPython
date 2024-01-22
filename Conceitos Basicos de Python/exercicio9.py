''' Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de 
calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício'''

horas_exercicio = float(input('Digite o número de horas de exercício físico por semana: '))

minutos_exercicio = horas_exercicio * 60
calorias_semana = minutos_exercicio * 5
calorias_mes = calorias_semana * 4  #(considerando 4 semanas em um mês)

print(f'O total de calorias queimadas em um mês é: {calorias_mes:.2f}')