texto = input("Ingresa una palabra: ")

def is_palindrome(palindromo):
    return palindromo == palindromo[::-1]


if is_palindrome(texto) == True:
    print("Es un palindromo.")
else:
    print("No es un palindromo.")
