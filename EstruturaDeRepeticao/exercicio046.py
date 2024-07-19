def calcular_media_saltos(saltos):
    # Ordena os saltos para eliminar o melhor e o pior
    saltos_ordenados = sorted(saltos)
    
    # Elimina o melhor (último elemento) e o pior (primeiro elemento)
    saltos_restantes = saltos_ordenados[1:-1]
    
    # Calcula a média dos saltos restantes
    media = sum(saltos_restantes) / len(saltos_restantes)
    
    return media

def main():
    atletas = []
    
    while True:
        nome_atleta = input("Digite o nome do atleta (ou enter para sair): ")
        
        if nome_atleta == "":
            break
        
        saltos = []
        for i in range(1, 6):
            while True:
                try:
                    distancia = float(input(f"Digite a distância do {i}º salto (em metros): "))
                    saltos.append(distancia)
                    break
                except ValueError:
                    print("Valor inválido. Digite novamente.")
        
        # Armazena os saltos e o nome do atleta em uma lista
        atletas.append((nome_atleta, saltos))
        
        # Calcula e exibe os resultados para o atleta atual
        print(f"\nResultado para o(a) atleta: {nome_atleta}\n")
        
        for i in range(5):
            print(f"{i+1}º Salto: {saltos[i]} m")
        
        melhor_salto = max(saltos)
        pior_salto = min(saltos)
        media = calcular_media_saltos(saltos)
        
        print(f"\nMelhor salto:  {melhor_salto} m")
        print(f"Pior salto: {pior_salto} m")
        print(f"Média dos demais saltos: {media} m\n")
    
    # Exibe o resultado final para todos os atletas
    print("\nResultado final:")
    for atleta in atletas:
        nome_atleta, saltos = atleta
        media_final = calcular_media_saltos(saltos)
        print(f"{nome_atleta}: {media_final} m")

if __name__ == "__main__":
    main()
