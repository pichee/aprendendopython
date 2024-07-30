def retangulo(x):
    while True:
        linhas = int(input("Quantas linhas você quer: "))
        colunas = int(input("Quantas colunas você quer: "))
        if linhas > 20:
            linhas = 20
        elif linhas < 1:
            linhas = 1
        if colunas > 20:
            colunas = 20
        elif colunas < 1:
            colunas = 1

        desenho = input("Digite qual desenho você quer: +, -, | \n")
        if desenho in ['+', '-', '|']:
            break
        else:
            print("Por favor, digite um desenho válido: +, -, |")

    print(desenho * colunas)
    for _ in range(linhas - 2):
        print(desenho + " " * (colunas - 2) + desenho)
    if linhas > 1:
        print(desenho * colunas)

retangulo(0)