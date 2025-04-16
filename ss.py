def is_palindrome(text):

    text = text.lower()

    #Acentos
    for acento, sinacento in (
        ("á", "a"), ("é", "e"), ("í", "i"),
        ("ó", "o"), ("ú", "u"),
    ):
        text = text.replace(acento, sinacento)

    #Caracteres =! de alfabeto -> "", vacio
    limpio = ''.join(c for c in text if c.isalnum())

    return limpio == limpio[::-1]


if __name__ == '__main__':
    texto = input("Ingresa una palabra o frase: ")
    if is_palindrome(texto):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")
