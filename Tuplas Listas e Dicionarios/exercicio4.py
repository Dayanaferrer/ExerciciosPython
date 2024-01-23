
# Crie um dicionário representando contatos(nome, telefone). Permita ao usuário procurar por um contato pelo nome.

contatos = {}

contatos['Ada'] = '18255-7890'
contatos['Grace Hopper'] = '91993-85666'
contatos['Katie Bouman'] = '3455-9012'

nome = input("Digite o nome do contato que você está procurando: ")
nome = nome.lower()

if nome in contatos:
    print(f"O número de telefone de {nome.title()} é {contatos[nome]}")
else:
    print(f"Desculpe, não existe um contato com o nome {nome.title()}")