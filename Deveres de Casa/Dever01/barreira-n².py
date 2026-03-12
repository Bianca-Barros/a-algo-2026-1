import random
import time

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

tamanhos = [1000, 5000, 10000, 20000, 50000]

for n in tamanhos:

    lista = [random.randint(0, 100000) for _ in range(n)]
    lista1 = lista.copy()
    lista2 = lista.copy()

    inicio = time.time()
    insertion_sort(lista1)
    fim = time.time()
    tempo_insertion = fim - inicio

    inicio = time.time()
    sorted(lista2)
    fim = time.time()
    tempo_sorted = fim - inicio

    print(f"n = {n}")
    print(f"Insertion Sort: {tempo_insertion:.6f} segundos")
    print(f"sorted() (timsort): {tempo_sorted:.6f} segundos")

"""
n = 1000
Insertion Sort: 0.027137 segundos
sorted() (Timsort): 0.000200 segundos
n = 5000
Insertion Sort: 0.762892 segundos
sorted() (Timsort): 0.001247 segundos
n = 10000
Insertion Sort: 4.760010 segundos
sorted() (Timsort): 0.001954 segundos
n = 20000
Insertion Sort: 15.004998 segundos
sorted() (Timsort): 0.004474 segundos
n = 50000
Insertion Sort: 116.727960 segundos
sorted() (Timsort): 0.013714 segundos
"""

"""
Nos testes, dá para ver que com listas pequenas a diferença é mínima, mas quando o tamanho da lista aumenta o Insertion Sort fica bem mais lento, enquanto o sorted() continua rápido.
"""
