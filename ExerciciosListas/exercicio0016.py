#Utilize uma lista para resolver o problema a seguir. 
#Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados
salario_faixas = [0] * 9
vendas = [3000, 1500, 7000, 4000, 500, 6000, 850, 3200, 10000]

for venda in vendas:
    salario_base = 200
    comissao = 0.09 * venda
    salario = salario_base + comissao
    
    if salario >= 1000:
        posicao = 8
    else:
        posicao = (int(salario) - 200) // 100
    
    salario_faixas[posicao] += 1

faixas = ["$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599", "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999", "$1000 em diante"]
for i, contador in enumerate(salario_faixas):
    print(f"Faixa {faixas[i]}: {contador} vendedores")
