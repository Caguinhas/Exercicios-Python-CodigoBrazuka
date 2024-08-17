divi = 0
soma = 0
notas = 0

while notas != -1:
    notas = float(input("Digite suas notas para saber a média:"))
    divi += 1
    soma = soma + notas
    resul = soma / divi

print("A média de suas notas é:", resul)
