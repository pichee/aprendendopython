def caixa_registradora(precos_produtos, dinheiro_fornecido):
    while True:
        print("Lojas Tabajara")
        total = 0
        produto_numero = 1

        for preco in precos_produtos:
            if preco == 0:
                break
            total += preco
            print(f"Produto {produto_numero}: R$ {preco:.2f}")
            produto_numero += 1
        
        print(f"Total: R$ {total:.2f}")
        
        dinheiro = dinheiro_fornecido
        print(f"Dinheiro: R$ {dinheiro:.2f}")
        
        troco = dinheiro - total
        print(f"Troco: R$ {troco:.2f}\n")
        
        break

precos_produtos = [2.20, 5.80, 0]  # Os preços dos produtos, terminando com 0 para indicar o fim
dinheiro_fornecido = 20.00  # Dinheiro fornecido pelo cliente

caixa_registradora(precos_produtos, dinheiro_fornecido)