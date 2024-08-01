#Leet spek generator. Leet é uma forma de se #escrever o alfabeto latino usando outros símbolos #em lugar das letras, como números por exemplo. A #própria palavra leet admite muitas variações, como #l33t ou 1337. O uso do leet reflete uma subcultura #relacionada ao mundo dos jogos de computador e #internet, sendo muito usada para confundir os #iniciantes e afirmar-se como parte de um grupo.
#Pesquise sobre as principais formas de traduzir as #letras. Depois, faça um programa que peça uma texto #e transforme-o para a grafia leet speak.
leet_dict = {
    'A': '4', 'B': '8', 'C': '(', 'D': '|)', 'E': '3', 'F': '|=',
    'G': '6', 'H': '#', 'I': '1', 'J': '_|', 'K': '|<', 'L': '1',
    'M': '/\\/\\', 'N': '/\\/', 'O': '0', 'P': '|*', 'Q': '0,',
    'R': '|2', 'S': '5', 'T': '7', 'U': '|_', 'V': '\\/',
    'W': '\\/\\/', 'X': '><', 'Y': '`/', 'Z': '2'
}

texto = input("Digite um texto para converter em Leet Speak: ")

leet_texto = ""
for char in texto.upper():  
    if char in leet_dict:
        leet_texto += leet_dict[char]
    else:
        leet_texto += char
print("Texto em Leet Speak:", leet_texto)