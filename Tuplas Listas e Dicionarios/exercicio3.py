''' Crie um dicionário representando um carrinho de compras. Adicione produtos(chaves) e 
quantidades(valores) ao carrinho. Calcule o total do carrinho de compra'''

carrinho = {}

carrinho['Maçãs'] = 3
carrinho['Bananas'] = 12
carrinho['Laranjas'] = 6

precos = {}
precos['Maçãs'] = 2.59 
precos['Bananas'] = 0.72  
precos['Laranjas'] = 1.85

total = sum(carrinho[produto] * precos[produto] for produto in carrinho)

print(f"O total do carrinho de compra é: {total}")