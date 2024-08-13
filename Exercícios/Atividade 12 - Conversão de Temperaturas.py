temp = int(input("Digite a temperatura em graus Celsius para saber a temperatura em Fahrenheit e Kelvin:"))

fah = ((temp * 9/5) + 32)
kel = (temp + 273.15)


print("Em celsius é de %d\xb0graus \n"
      "Em Fahrenheit é de %d\xb0graus \n"
      "Em Kelvin é %d\xb0graus" % (temp, fah, kel))