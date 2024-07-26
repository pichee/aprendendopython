cpf = [0] * 9
while True:
    numero = input("Digite seu CPF (9 dígitos): ")
    if len(numero) != 9 or not numero.isdigit():
        print("Digite um CPF válido com 9 dígitos.")
    else:
        print(f"CPF: {numero}")
        for a in range(9):
            cpf[a] = int(numero[a])
        break  
a = 10
aux = 8
multiplica = [0] * 9
while a > 1:
    multiplica[aux] = cpf[aux] * a
    a -= 1
    aux -= 1
soma = sum(multiplica)
print(f"Resultado da multiplicação: {soma}")
soma = soma * 10
print(f"Resultado da outra multiplicação por 10: {soma}")
soma = soma % 11
print(f"Resto da divisão por 11: {soma}")
if soma > 9:
    print("0")
else:
    print(f"{soma}")