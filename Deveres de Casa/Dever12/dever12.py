import math


class BellmanFord:
    #implementa o algoritmo

    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = []

    def adicionar_aresta(
        self,
        origem,
        destino,
        peso
    ):

        self.arestas.append(
            (origem, destino, peso)
        )

    def executar(self, origem_inicial):
        #executa o algoritmo

        distancias = {
            vertice: math.inf
            for vertice in self.vertices
        }

        predecessores = {
            vertice: None
            for vertice in self.vertices
        }

        distancias[origem_inicial] = 0

        for iteracao in range(
            len(self.vertices) - 1
        ):

            print(f"\nIteração {iteracao + 1}")
            print("-" * 40)

            for origem, destino, peso in self.arestas:

                if (
                    distancias[origem]
                    != math.inf
                    and (
                        distancias[origem]
                        + peso
                        < distancias[destino]
                    )
                ):

                    distancias[destino] = (
                        distancias[origem]
                        + peso
                    )

                    predecessores[destino] = (
                        origem
                    )

            for vertice in self.vertices:

                print(
                    f"Vértice {vertice}: "
                    f"Distância = "
                    f"{distancias[vertice]}, "
                    f"Predecessor = "
                    f"{predecessores[vertice]}"
                )

        ciclo_negativo = False

        for origem, destino, peso in self.arestas:

            if (
                distancias[origem]
                != math.inf
                and (
                    distancias[origem]
                    + peso
                    < distancias[destino]
                )
            ):

                ciclo_negativo = True

        print("\nVerificação:")

        if ciclo_negativo:
            print("Existe ciclo negativo.")
        else:
            print("Não existe ciclo negativo.")


def main():

    vertices = [0, 1, 2, 3, 4]

    grafo = BellmanFord(vertices)

    grafo.adicionar_aresta(0, 1, 5)
    grafo.adicionar_aresta(1, 2, 1)
    grafo.adicionar_aresta(1, 3, 2)
    grafo.adicionar_aresta(2, 4, 1)
    grafo.adicionar_aresta(4, 3, -1)

    grafo.executar(0)


if __name__ == "__main__":
    main()

"""

Iteração 1
----------------------------------------
Vértice 0: Distância = 0, Predecessor = None
Vértice 1: Distância = 5, Predecessor = 0
Vértice 2: Distância = 6, Predecessor = 1
Vértice 3: Distância = 6, Predecessor = 4
Vértice 4: Distância = 7, Predecessor = 2

Iteração 2
----------------------------------------
Vértice 0: Distância = 0, Predecessor = None
Vértice 1: Distância = 5, Predecessor = 0
Vértice 2: Distância = 6, Predecessor = 1
Vértice 3: Distância = 6, Predecessor = 4
Vértice 4: Distância = 7, Predecessor = 2

Iteração 3
----------------------------------------
Vértice 0: Distância = 0, Predecessor = None
Vértice 1: Distância = 5, Predecessor = 0
Vértice 2: Distância = 6, Predecessor = 1
Vértice 3: Distância = 6, Predecessor = 4
Vértice 4: Distância = 7, Predecessor = 2

Iteração 4
----------------------------------------
Vértice 0: Distância = 0, Predecessor = None
Vértice 1: Distância = 5, Predecessor = 0
Vértice 2: Distância = 6, Predecessor = 1
Vértice 3: Distância = 6, Predecessor = 4
Vértice 4: Distância = 7, Predecessor = 2

Verificação:
Não existe ciclo negativo.

"""
