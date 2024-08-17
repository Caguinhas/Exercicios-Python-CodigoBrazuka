def contar_vogais(texto):
    # Convertemos o texto para minúsculas para facilitar a contagem
    texto = texto.lower()

    # Definimos as vogais
    vogais = 'aeiou'

    # Inicializamos a contagem de vogais em 0
    contagem = 0

    # Percorremos cada caractere do texto
    for caractere in texto:
        # Verificamos se o caractere é uma vogal
        if caractere in vogais:
            contagem += 1



# Exemplo de uso
texto = "Olá, Mundo!"
numero_de_vogais = contar_vogais(texto)
print(f"O número de vogais em '{texto}' é: {numero_de_vogais}")