# NP 
class SubsetSum:
    """Resolve o problema Subset Sum."""

    def __init__(self, conjunto, alvo):
        """Inicializa o conjunto e o valor alvo."""

        self.conjunto = conjunto
        self.alvo = alvo

    def encontrar_subconjunto(
        self,
        indice=0,
        soma_atual=0,
        subconjunto=None
    ):
        """Busca um subconjunto cuja soma seja igual ao alvo."""

        if subconjunto is None:
            subconjunto = []

        if soma_atual == self.alvo:
            return subconjunto

        if indice == len(self.conjunto):
            return None

        resultado = self.encontrar_subconjunto(
            indice + 1,
            soma_atual + self.conjunto[indice],
            subconjunto + [self.conjunto[indice]]
        )

        if resultado is not None:
            return resultado

        return self.encontrar_subconjunto(
            indice + 1,
            soma_atual,
            subconjunto
        )


def main():
    """Executa os exemplos do exercício."""

    casos_teste = [
        ([2, 4, 6, 10], 16),
        ([-5, -2, 1, 3, 7, 12, 15, 21], 0),
        (
            [
                12345, 87654, 43210, 54321, 11111,
                22222, 33333, 44444, 55555, 66666,
                77777, 88888, 99999, 13579, 24680,
                11223, 44556, 77889, 99000, 31415,
                27182, 16180, 14142, 17320, 22360,
                26457, 31622, 44721, 50000, 60000
            ],
            500000
        )
    ]

    for conjunto, alvo in casos_teste:

        problema = SubsetSum(
            conjunto,
            alvo
        )

        resultado = (
            problema.encontrar_subconjunto()
        )

        print(f"\nConjunto: {conjunto}")
        print(f"Alvo: {alvo}")

        if resultado is not None:
            print(
                "Subconjunto encontrado:"
            )
            print(resultado)
        else:
            print(
                "Não existe subconjunto "
                "com essa soma."
            )


"""

Conjunto: [2, 4, 6, 10]
Alvo: 16
Subconjunto encontrado:
[2, 4, 10]

Conjunto: [-5, -2, 1, 3, 7, 12, 15, 21]
Alvo: 0
Subconjunto encontrado:
[]

Conjunto: [12345, 87654, 43210, 54321, 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999, 13579, 24680, 11223, 44556, 77889, 99000, 31415, 27182, 16180, 14142, 17320, 22360, 26457, 31622, 44721, 50000, 60000]
Alvo: 500000
Subconjunto encontrado:
[12345, 87654, 43210, 54321, 11111, 22222, 33333, 44444, 13579, 27182, 14142, 26457, 50000, 60000]

if __name__ == "__main__":
    main()
"""
