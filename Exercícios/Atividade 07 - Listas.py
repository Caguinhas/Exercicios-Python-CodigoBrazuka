lista = ["Morango", "Arroz", "Panela", "Vassoura"]

a = 0

while a != "1":
    a = input("Bem vindo a lista de compras! Digite para adicionar novos produtos ou digite 1 para sair: ")
    lista.append(a)
    if a == "1":
        lista.remove(a)

print(lista)
