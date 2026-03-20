import math

#função recursiva
def f_recursivo(n):
   
    #caso base
    if n == 1:
        return 2

    #caso recursivo
    return 2 * f_recursivo(n - 1) + n ** 2

#função usando formula fechada
def f_fechada(n):
    #fórmula derivada da recorrência
    return int(6 * (2 ** n) - (n ** 2 + 4 * n + 6))


def main():

    n = int(input("Digite um valor para n: "))
    
    #cálculo
    resultado_rec = f_recursivo(n)
    resultado_fec = f_fechada(n)
    
    #saída 
    print(f"F({n}) recursivo = {resultado_rec}")
    print(f"F({n}) fórmula fechada = {resultado_fec}")


if __name__ == "__main__":
    main()
"""
Digite um valor para n: 20
F(20) recursivo = 6815258
F(20) fórmula fechada = 6290970
"""
