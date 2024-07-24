#Faça um programa que receba a temperatura média de #cada mês do ano e armazene-as em uma lista. Após #isto, calcule a média anual das temperaturas e #mostre todas as temperaturas acima da média anual, #e em que mês elas ocorreram (mostrar o mês por #extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
meses = []
soma = 0.0

for a in range(12):   
    temp = float(input(f"Qual a média da temperatura do mês {a + 1}: "))
    meses.append(temp)
    soma += temp

media_anual = soma / 12

print(f"\nMédia das temperaturas é: {media_anual:.2f}\n")

# Dicionário para mapear número do mês para o nome do mês por extenso
meses_extenso = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

print("Temperaturas acima da média anual:")
for i in range(12):
    if meses[i] > media_anual:
        print(f"{meses_extenso[i + 1]}: {meses[i]:.2f}")