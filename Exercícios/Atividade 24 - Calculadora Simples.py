print("Bem-vindo a calculadora simples!")

x = str(input(
        'Digite o operador que deseja para realizar um cálculo com dois números(+, -, *, /).Ou digite s para sair: '))

while x != "s":
    if x == '+':
        num1 = int(input("Digite o primeiro número:"))
        num2 = int(input("Digite o segundo número:"))
        soma = num1 + num2

        print(f"{num1} + {num2} = {soma}")
        break

    elif x == '-':
        num1 = int(input("Digite o primeiro número:"))
        num2 = int(input("Digite o segundo número:"))
        sub = num1 - num2

        print(f"{num1} + {num2} = {soma}")
        break
