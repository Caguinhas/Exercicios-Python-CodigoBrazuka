def np(numero):
    soma = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma += i

    return soma == numero

numero = int(input("Digite um número: "))
if np(numero):
    print(f"{numero} é um número perfeito!")
else:
    print(f"{numero} não é um número perfeito.")