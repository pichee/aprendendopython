#Valida e corrige número de telefone. Faça um #programa que leia um número de telefone, e corrija #o número no caso deste conter somente 7 dígitos, #acrescentando o '3' na frente. O usuário pode #informar o número com ou sem o traço separador.
#Valida e corrige número de telefone
#Telefone: 461-0133
#Telefone possui 7 dígitos. Vou acrescentar o digito #três na frente.
#Telefone corrigido sem formatação: 34610133
#Telefone corrigido com formatação: 3461-0133
def telefone():
    numero = input("Digite seu número de telefone: ")

    numero = numero.replace('-', '')
    
    tamanho = len(numero)
    
    if tamanho < 7:
        print("Coloque pelo menos 7 números.")
        return
    elif tamanho > 8:
        print("Isso não pode ser um número de telefone válido.")
        return
    elif tamanho == 7:
        print("Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.")
        numero = '3' + numero
    print(f"Telefone corrigido sem formatação: {numero}")
    telefone_formatado = numero[:4] + '-' + numero[4:]
    print(f"Telefone corrigido com formatação: {telefone_formatado}")

telefone()