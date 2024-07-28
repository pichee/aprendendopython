#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o
#  custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def funcao(x):
    i=float(input("Digite o valor do item"))
    imposto=float(input("Digite o valor do imposto em %"))
    valortotal=(imposto/100)+i
    print(f"O valor do item {i} mais o imposto de {imposto} o preço final sera {valortotal:.2f}")


funcao(0)
