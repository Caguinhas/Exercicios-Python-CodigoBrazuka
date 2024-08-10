def e_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primos_intervalo(inicio, fim):
    return [num for num in range(inicio, fim + 1) if e_primo(num)]

inicio = int(input("Início do intervalo: "))
fim = int(input("Final do intervalo: "))

print(f"Números primos entre {inicio} e {fim}: {primos_intervalo(inicio, fim)}")