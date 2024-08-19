import random

sorte = random.randint(1, 100)

palpite = int(input("Jogo de adivinhação. Digite um número de 1 a 100 para tentar adivinhar: "))

while palpite != sorte:

    if palpite > sorte:
        palpite = int(input(f"Você não acertou o número da sorte é menor que o {palpite}. Tente novamente: "))

    elif palpite < sorte:
        palpite = int(input(f"Você não acertou o número da sorte é maior que o {palpite}. Tente novamente: "))

print(f"Parabéns, você acertou! O número da sorte é o {sorte}")