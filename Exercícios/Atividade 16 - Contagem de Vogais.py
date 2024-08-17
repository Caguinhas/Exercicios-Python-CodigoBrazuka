def func(frase):
    vogal = ("aeiou")
    contagem = 0

    for i in frase:
        if i in vogal:
            contagem += 1

    return contagem

frase = str(input("Digite uma frase para saber o número de vogais:"))
num_resultado = func(frase)
print("A frase possui", num_resultado,"vogais")
