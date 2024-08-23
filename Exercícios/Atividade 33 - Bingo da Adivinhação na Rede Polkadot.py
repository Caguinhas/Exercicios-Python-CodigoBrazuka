import random

fila = random.sample(range(1, 75), 5)

numeros = []
x = 0
tentativas = 0
sorte = 0

for i in range(1, 75 + 1):
        numeros.append(i)

while fila:
    a = random.choice(numeros)
    x += 1

    while sorte != a:
        print(f"Cartela: {fila}")
        print(f"Números não sorteados: {numeros}")
        sorte = int(input("Digite um número: "))

        if sorte == a:
            if sorte in fila:
                print(f"Parabéns, você acertou! O número sorteado foi o {a}")
                fila.remove(a)
            else:
                print(f"O número sorteado foi o {a}, mas não está na cartela.")

            numeros.remove(a)
            print(f"Números restantes na cartela: {fila}")

        else:
            print("Número incorreto, tente novamente.")

print(f"Parabéns! Você completou a cartela com um total de {x} sorteios.")