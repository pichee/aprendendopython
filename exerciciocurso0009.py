palavra_s=input("Digite a palavra secreta:")
tamanho=len(palavra_s)
contador=int(0)
ver_palavra=["*"]*tamanho
while "".join(ver_palavra)!=palavra_s:
    print("Tente adivinhar a palavra secreta:{}\n".format(ver_palavra))
    letra=input("Digite uma letra:")
    i=0
    contador+=1
    for i in range(tamanho):
        if(letra==palavra_s[i]):
         ver_palavra[i]=palavra_s[i]


print("parabéns você achou a palavra")
print("Em {} tentativas".format(contador))