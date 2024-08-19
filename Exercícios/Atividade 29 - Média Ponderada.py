def mp():
    for i in range(3):
        num1 = int(input("Digite a primeira nota que possui peso 2: "))
        num2 = int(input("Digite a primeira nota que possui peso 3: "))
        num3 = int(input("Digite a primeira nota que possui peso 5: "))

        resul = ((num1 * 2) + (num2 * 3) + (num3 * 5)) / 10

        return resul

mediap = mp()
print(f"A sua média foi de {mediap}")
