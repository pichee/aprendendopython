produtos = [
    {'nome': 'leite', 'preco': 2.00},
    {'nome': 'pão', 'preco': 0.15},
    {'nome': 'sushi', 'preco': 99.99},
    {'nome': 'peixe', 'preco': 15},
    {'nome': 'codorna', 'preco': 857.01}
]
for produto in produtos:
    produto['preco'] += produto['preco'] * 0.1
tamanho = len(produtos)
print(f"Tamanho: {tamanho}")
for i in range(tamanho):
    for j in range(0, tamanho - i - 1):
        if produtos[j]['nome'] > produtos[j + 1]['nome']:
            produtos[j], produtos[j + 1] = produtos[j + 1], produtos[j]
for i in range(tamanho):
    for j in range(0, tamanho - i - 1):
        if produtos[j]['preco'] > produtos[j + 1]['preco']:
            produtos[j], produtos[j + 1] = produtos[j + 1], produtos[j]
            
                
    