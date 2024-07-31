#Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
cpf=input("Digite o seu CPF:")
tamanho=len(cpf)
cpf=int(cpf)
if tamanho==9:
    print("CPF valido")
else:
    print("CPF invalido")    