def poli(frase):
    if frase == frase[: : -1]:
        print("A frase ou palavra é um palíndromo")
    else:
        print("A frase não é um palíndromo")

frase = str(input("Digite uma frase ou palavra: "))

poli(frase)