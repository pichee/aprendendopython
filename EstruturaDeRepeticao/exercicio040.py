maior = 0
menor = 99999999
soma = 0
soma2000 = 0
contagem2000 = 0

cidade_maior = 0
cidade_menor = 0

for a in range(5):
    city = int(input("Digite o código da cidade: "))
    numerop = int(input("Digite o número de veículos de passeio: "))
    numeroa = int(input("Digite o número de acidentes de trânsito com vítima: "))
    indice = numeroa / numerop
    
    if maior < indice:
        maior = indice
        cidade_maior = city
    if menor > indice:
        menor = indice
        cidade_menor = city
    
    soma += numerop
    if numerop < 2000:
        soma2000 += numeroa
        contagem2000 += 1

media_veiculos = soma / 5

if contagem2000 > 0:
    media_acidentes_2000 = soma2000 / contagem2000
else:
    media_acidentes_2000 = 0

print(f"Maior índice de acidentes: {maior}, Cidade: {cidade_maior}")
print(f"Menor índice de acidentes: {menor}, Cidade: {cidade_menor}")
print(f"Média de veículos nas cinco cidades: {media_veiculos}")
print(f"Média de acidentes de trânsito nas cidades com menos de 2000 veículos: {media_acidentes_2000}")