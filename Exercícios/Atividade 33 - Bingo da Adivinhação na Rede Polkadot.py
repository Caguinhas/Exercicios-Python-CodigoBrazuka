import random

fila = random.sample(range(1, 75), 5)

numeros = []
x = 0
tentativas = 0
sorte = 0

for i in range(1, 75 + 1):
        numeros.append(i)

while fila != []:
    a = random.choice(numeros)
    numeros.remove(a)
    x += 1

    while sorte != a and a != fila:
        print(f"Cartela: {fila}")
        print(f"Números não sorteados {numeros}")
        sorte = int(input("Digite um número: "))

        if sorte == a and a in fila:
            print(f"Parabéns, você acertou! O número sorteado foi o {a}")
            fila.remove(a)
            print(f"Números restantes na cartela: {fila}")

        elif sorte == a and a not in fila:
            print(f"Parabéns, você acertou! O número sorteado foi o {a}, mas o número sorteado não está na cartela")

        else:
            print("Número incorreto, tente novamente")

print(f"Parabéns! Você completou a cartela com um total de {x} sorteios")