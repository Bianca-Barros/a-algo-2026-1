# função recursiva para verificar se o array é palindromo
def eh_palindromo(array, inicio, fim):

    # se os índices se cruzarem ou forem iguais significa que todos os elementos foram verificados
    if inicio >= fim:
        return True

    # se os elementos das extremidades forem diferentes
    if array[inicio] != array[fim]:
        return False

    # chamada recursiva verificando o restante do array
    return eh_palindromo(array, inicio + 1, fim - 1)


# ex
array1 = [1, 2, 3, 2, 2, 3, 2, 1]
array2 = ["e", "r", "r", "o", "u"]
array3 = ["a", "s", "a"]
array4 = ["b", "i", "a", "n", "c", "a"]

# tests
print(eh_palindromo(array1, 0, len(array1)-1))
print(eh_palindromo(array2, 0, len(array2)-1))
print(eh_palindromo(array3, 0, len(array3)-1))
print(eh_palindromo(array4, 0, len(array4)-1))

# respostas 
"""
True
False
True
False
"""
