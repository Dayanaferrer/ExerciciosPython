'''Escreva um programa que calcule o tempo de uma viagem. 
Faça um comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração: Avião=600km/h - Carro=100km/h - Ônibus=80km/h. '''

distancia = float(input('Digite a distância da viagem em quilômetros: '))

velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

tempo_aviao = distancia / velocidade_aviao
tempo_carro = distancia / velocidade_carro
tempo_onibus = distancia / velocidade_onibus

# Converter horas para minutos e segundos
horas_aviao, resto_aviao = divmod(tempo_aviao, 1)
minutos_aviao, segundos_aviao = divmod(resto_aviao * 60, 1)
segundos_aviao = segundos_aviao * 60

horas_carro, resto_carro = divmod(tempo_carro, 1)
minutos_carro, segundos_carro = divmod(resto_carro * 60, 1)
segundos_carro = segundos_carro * 60

horas_onibus, resto_onibus = divmod(tempo_onibus, 1)
minutos_onibus, segundos_onibus = divmod(resto_onibus * 60, 1)
segundos_onibus = segundos_onibus * 60

print(f'Tempo de viagem de avião: {int(horas_aviao)} horas, {int(minutos_aviao)} minutos e {int(segundos_aviao)} segundos')
print(f'Tempo de viagem de carro: {int(horas_carro)} horas, {int(minutos_carro)} minutos e {int(segundos_carro)} segundos')
print(f'Tempo de viagem de ônibus: {int(horas_onibus)} horas, {int(minutos_onibus)} minutos e {int(segundos_onibus)} segundos')
