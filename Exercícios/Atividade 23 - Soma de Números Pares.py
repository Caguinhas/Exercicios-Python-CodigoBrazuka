soma = 0

for i in range(1, 101):
    if i % 2 == 0:
        soma = soma + i
        if i != 100:
            print(f"{i} +", end=" ")

print("100 =", soma)
