n = int(input("Digite um número para calcular a soma de todos os seus antencessores até ele: "))

soma = 0
n += 1

for i in range(n):
    soma = soma + i
    print(f"{i} +", end=" ")

print(f"= {soma}")