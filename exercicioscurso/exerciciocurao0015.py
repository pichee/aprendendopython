
perguntas_respostas = {
    "primeirapergunta": "Quem descobriu o Brasil",
    "questionario_primeira_pergunta": "1)marcelo\n2)pele\n3)Diego Maradona\n4)Cristovo colombo",
    "segundapergunta": "Quem é o maior jogador de gut da história",
    "questionario_segunda_pergunta": "1)marcelo\n2)pele\n3)Diego Maradona\n4)Cristovo colombo"
}

respostas_corretas = {
    "primeirapergunta": "4",
    "segundapergunta": "1"
}

acertos = 0

print(perguntas_respostas["primeirapergunta"])
print(perguntas_respostas["questionario_primeira_pergunta"])
resposta_usuario = input("Digite o número da resposta correta: ")

if resposta_usuario == respostas_corretas["primeirapergunta"]:
    acertos += 1

print(perguntas_respostas["segundapergunta"])
print(perguntas_respostas["questionario_segunda_pergunta"])
resposta_usuario = input("Digite o número da resposta correta: ")

if resposta_usuario == respostas_corretas["segundapergunta"]:
    acertos += 1

print(f"Você acertou {acertos} de {len(respostas_corretas)} perguntas.")