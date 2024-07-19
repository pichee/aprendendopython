#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#Maior e Menor Acerto;
#Total de Alunos que utilizaram o sistema;
#A Média das Notas da Turma.
#Gabarito da Prova:
#01 - A
#02 - B
#03 - C
#04 - D
#05 - E
#06 - E
#07 - D
#08 - C
#09 - B
#10 - A
#Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
numero1=input("Digite o gabarito da questao 1:")
numero2=input("Digite o gabarito da questao 2:")
numero3=input("Digite o gabarito da questao 3:")
numero4=input("Digite o gabarito da questao 4:")
numero5=input("Digite o gabarito da questao 5:")
numero6=input("Digite o gabarito da questao 6:")
numero7=input("Digite o gabarito da questao 7:")
numero8=input("Digite o gabarito da questao 8:")
numero9=input("Digite o gabarito da questao 9:")
numero10=input("Digite o gabarito da questao 10:")
a=1
contador=0
soma=0
alunos=1
maior=0
menor=11
while True:
    contador=0
    acerto1=input(f"Digite o que o aluno colocou na questao 1:")
    acerto2=input(f"Digite o que o aluno colocou na questao 2:")
    acerto3=input(f"Digite o que o aluno colocou na questao 3:")
    acerto4=input(f"Digite o que o aluno colocou na questao 4:")
    acerto5=input(f"Digite o que o aluno colocou na questao 5:")
    acerto6=input(f"Digite o que o aluno colocou na questao 6:")
    acerto7=input(f"Digite o que o aluno colocou na questao 7:")
    acerto8=input(f"Digite o que o aluno colocou na questao 8:")
    acerto9=input(f"Digite o que o aluno colocou na questao 9:")
    acerto10=input(f"Digite o que o aluno colocou na questao 10:")
    if acerto1==numero1:
        contador=0+1
    if acerto2==numero2:
        contador=0+1
    if acerto3==numero3:
        contador=0+1
    if acerto4==numero4:
        contador=0+1
    if acerto5==numero5:
        contador=0+1
    if acerto6==numero6:
        contador=0+1
    if acerto7==numero7:
        contador=0+1
    if acerto8==numero8:
        contador=0+1
    if acerto9==numero9:
        contador=0+1
    if acerto10==numero10:
        contador=0+1
    if maior<contador:
        maior=contador
    if menor>contador:
        menor=contador
    decisao=input("Voce quer adicionar mais algum aluno?[s] ou [n]")
    soma=contador+soma
    if decisao=='n':
        break
    else:
        alunos=alunos+1

soma=soma/alunos
print(f"O maior aluno teve nota {maior} e o menor nota {menor} já a media das notas foi {soma}")
