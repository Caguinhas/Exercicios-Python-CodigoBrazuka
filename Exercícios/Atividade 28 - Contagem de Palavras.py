def contador(frase):

    divisao = frase.split()


    return len(divisao)

frase = input("Digite uma frase: ")

quantidade_palavras = contador(frase)

print(f"A frase possui {quantidade_palavras} palavras.")