fatorial = int(input("Digite um número para saber o resultado de seu fatorial:"))

calculo = fatorial + 1


x = 1

while fatorial >= 2:
    print(fatorial, "x ", end="")
    fatorial -= 1

print("1 = ", end="")

for i in range(1, calculo):
    x = x * i

print(x)



