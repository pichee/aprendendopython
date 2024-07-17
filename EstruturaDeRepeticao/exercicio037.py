# Inicialização das variáveis para armazenar os valores desejados
mais_alto = 0
mais_baixo = 0
mais_gordo = 0
mais_magro = 0
peso_menor = 9999999
peso_maior = 0
media_altura = 0
media_peso = 0
total_clientes = 0

while True:
    # Entrada de dados do usuário
    codigo = int(input("Digite o Código do aluno (ou 0 para sair): "))
    
    if codigo == 0:
        break  # Encerra o loop quando o usuário digita 0
    
    altura = float(input("Digite a altura do aluno: "))
    peso = float(input("Digite o peso do aluno: "))
    
    # Atualização das estatísticas gerais
    media_altura += altura
    media_peso += peso
    total_clientes += 1
    
    # Verificação para encontrar o mais alto e o mais baixo
    if altura > mais_alto:
        mais_alto = altura
        codigo_alto = codigo  # Armazena o código do cliente mais alto
    
    if altura < mais_baixo or mais_baixo == 0:
        mais_baixo = altura
        codigo_baixo = codigo  # Armazena o código do cliente mais baixo
    
    # Verificação para encontrar o mais gordo e o mais magro
    if peso > peso_maior:
        peso_maior = peso
        codigo_gordo = codigo  # Armazena o código do cliente mais gordo
    
    if peso < peso_menor:
        peso_menor = peso
        codigo_magro = codigo  # Armazena o código do cliente mais magro

# Cálculo das médias de altura e peso
if total_clientes > 0:
    media_altura /= total_clientes
    media_peso /= total_clientes

# Saída dos resultados
print("\nResultados:")
print(f"Código do cliente mais alto: {codigo_alto}, Altura: {mais_alto}m")
print(f"Código do cliente mais baixo: {codigo_baixo}, Altura: {mais_baixo}m")
print(f"Código do cliente mais gordo: {codigo_gordo}, Peso: {peso_maior}kg")
print(f"Código do cliente mais magro: {codigo_magro}, Peso: {peso_menor}kg")
print(f"Média das alturas dos clientes: {media_altura:.2f}m")
print(f"Média dos pesos dos clientes: {media_peso:.2f}kg")
