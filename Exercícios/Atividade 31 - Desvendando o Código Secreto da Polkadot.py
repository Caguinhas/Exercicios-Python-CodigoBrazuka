num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

lista = []
total = 0

for i in range(num1, num2 + 1):
    lista.append(i)

    if i % 3 == 0 and i % 5 == 0:
        lista.remove(i)

    elif i % 3 == 0:
        total += i

    elif i % 5 == 0:
        total -= i

print("O código é:", total)