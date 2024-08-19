def primo(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        
    return True

def primosintervalo(inicio, fim):
    return [num for num in range(inicio, fim + 1) if primo(num)]

inicio = int(input("Início do intervalo: "))
fim = int(input("Final do intervalo: "))

print(f"Números primos entre {inicio} e {fim}: {primosintervalo(inicio, fim)}")