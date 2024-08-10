x = int(input("Qual a temperatura atual: "))

if x < 15:
    print("Nesse momento está fazendo frio")

elif x >= 15 and x <= 30:
    print("Nesse momento a temperatura está agradável")

else:
    print("Nesse momento está quente")