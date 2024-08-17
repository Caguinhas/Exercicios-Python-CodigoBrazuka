import random

print("Bem-vindo ao jogo de adivinhação!")

sorte = 0

numero = random.randint(1,10)

while sorte != numero:
    sorte = int(input("Tente adivinhar qual é o número. Digite um número de 1 a 100: "))

    if sorte == numero:
        print(f"Parabéns, você acertou! O número da sorte é o {numero}")
    else:
        print("Você errou, tente novamente")