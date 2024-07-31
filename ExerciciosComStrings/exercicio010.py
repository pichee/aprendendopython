#Número por extenso. Escreva um programa que #solicite ao usuário a digitação de um número até 99 #e imprima-o na tela por extenso.


def numero_por_extenso():
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    especiais = ["dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

    numero = int(input("Digite um número inteiro até 99: "))

    if numero < 0 or numero > 99:
        print("Número inválido")
        return

    if numero == 0:
        print("zero")
    elif 10 <= numero < 20:
        print(especiais[numero - 10])
    else:
        dezena = numero // 10
        unidade = numero % 10

        if dezena > 0:
            print(dezenas[dezena], end="")
            if unidade > 0:
                print(" e", end=" ")

        if unidade > 0:
            print(unidades[unidade])
        elif dezena > 0:
            print()

numero_por_extenso()