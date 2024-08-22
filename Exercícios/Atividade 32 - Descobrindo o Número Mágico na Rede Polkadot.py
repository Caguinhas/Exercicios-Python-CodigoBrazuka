def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def somando(num):
    soma = 0
    for i in str(num):
        soma += int(i)

    if soma % 2 != 0:
        return True

primos = []

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

for num in range(inicio, fim + 1):
     if eh_primo(num):
         if somando(num):
             # não existe número primo divisível por 4 kkk
             if num % 4 == 0:
                primos.append(num)

if primos:
    print(f"O número mágico é {primos[0]}")
else:
    print("O número mágico não foi encontrado")

