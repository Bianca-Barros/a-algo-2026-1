import time
import sys

sys.setrecursionlimit(2000) #aumentar o limite da recursao

def fatorial(n):
    if n == 0 or n == 1:
        return 1

    return n * fatorial(n - 1)

valores = [10, 100, 500, 1000]

for n in valores:

    inicio = time.time()

    resultado = fatorial(n)

    fim = time.time()

    tempo_execucao = fim - inicio

    print(f"n = {n}")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")

"""
n = 10
Tempo de execução: 0.000005 segundos
n = 100
Tempo de execução: 0.000022 segundos
n = 500
Tempo de execução: 0.000211 segundos
n = 1000
Tempo de execução: 0.000407 segundos
"""
"""
O algoritmo calcula o fatorial usando recursão, ou seja, a função chama ela mesma até chegar no caso base (0! = 1). Para calcular n!, a função é chamada cerca de n vezes, fazendo apenas uma verificação e uma multiplicação em cada chamada. Por isso, o tempo de execução cresce de forma linear, tendo complexidade O(n).
No teste com n = 1000, apareceu o erro RecursionError, porque o Python tem um limite de chamadas recursivas. Para resolver isso, foi usado sys.setrecursionlimit() para aumentar esse limite.
"""
