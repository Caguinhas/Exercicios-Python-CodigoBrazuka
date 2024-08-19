lista = []
i = 0

while i != -1:
    a = int(input("Digite um número positivo para colocar na lista, se quiser parar de adicionar, basta digitar -1: "))
    i = a
    if a != -1:
        lista.append(a)


menor = min(lista)
maior = max(lista)
soma = sum(lista)
quantidade = len(lista)

media = soma / quantidade

print(f"O menor número da lista é o {menor}, já o maior é o {maior}. A média de todos os números da lista é {media}")
