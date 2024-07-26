#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
#necessita da esfera;
#necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
problema = [0] * 4
total = 0

while True:
    mouses = int(input("Situação do mouse\n1- necessita da esfera\n2- necessita de limpeza\n3- necessita troca do cabo ou conector\n4- quebrado ou inutilizado\n"))
    if mouses == 0:
        break
    elif mouses > 4:
        print("Opção inválida")
    else:
        mouses = mouses - 1
        quantidade = int(input(f"Informe a quantidade de mouses que possuem o problema {mouses + 1}: "))
        total += quantidade
        problema[mouses] = problema[mouses] + quantidade

print(f"O total de mouses é {total}\n")

for i in range(4):
    porcentagem = (problema[i] / total) * 100 if total > 0 else 0
    print(f"Problema {i + 1}: {problema[i]} mouses ({porcentagem:.2f}%)")