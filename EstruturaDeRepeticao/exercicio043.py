#O cardápio de uma lanchonete é o seguinte:
#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

total = 0

while True:
    print("Cardápio:")
    print("Especificação   Código  Preço")
    print("Cachorro Quente 100     R$ 1,20")
    print("Bauru Simples   101     R$ 1,30")
    print("Bauru com ovo   102     R$ 1,50")
    print("Hambúrguer      103     R$ 1,20")
    print("Cheeseburguer   104     R$ 1,30")
    print("Refrigerante    105     R$ 1,00")

    codigo = int(input("O que você quer comprar (digite o código): "))

    if codigo == 100:
        quantidade = int(input("Você quer quantos: "))
        total += 1.20 * quantidade
    elif codigo == 101:
        quantidade = int(input("Você quer quantos: "))
        total += 1.30 * quantidade
    elif codigo == 102:
        quantidade = int(input("Você quer quantos: "))
        total += 1.50 * quantidade
    elif codigo == 103:
        quantidade = int(input("Você quer quantos: "))
        total += 1.20 * quantidade
    elif codigo == 104:
        quantidade = int(input("Você quer quantos: "))
        total += 1.30 * quantidade
    elif codigo == 105:
        quantidade = int(input("Você quer quantos: "))
        total += 1.00 * quantidade
    else:
        print("Código inválido. Tente novamente.")

    decisão = input("Vai pedir mais alguma coisa? (sim[s] ou não[n]): ").lower()
    if decisão == 'n':
        break

print("O total a pagar vai ser igual a R$ {:.2f}".format(total))