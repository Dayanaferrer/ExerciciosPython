''' Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, 
e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabelade conversão abaixo
                                Dólar Americano: R$4,91 
                                Peso Argentino: R$0,02 
                                Dólar Australiano: R$3,18 
                                Dólar Canadense: R$3,64 
                                Franco Suiço: R$0,42 
                                Euro: R$5,36 
                                Libra esterlina: R$6,21 '''


def converter_moeda(valor_em_reais):
    conversoes = {
        'Dólar Americano': 4.91,
        'Peso Argentino': 0.02,
        'Dólar Australiano': 3.18,
        'Dólar Canadense': 3.64,
        'Franco Suiço': 0.42,
        'Euro': 5.36,
        'Libra esterlina': 6.21
    }

    for moeda, taxa in conversoes.items():
        valor_convertido = valor_em_reais / taxa
        print(f'Com R${valor_em_reais}, você pode comprar {valor_convertido:.2f} {moeda}')

valor_em_reais = float(input("Insira quanto dinheiro você tem na carteira (em reais): "))

converter_moeda(valor_em_reais)

