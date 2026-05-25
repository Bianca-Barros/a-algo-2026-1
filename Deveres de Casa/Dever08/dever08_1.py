import heapq


class Grafo:
    #grafo ponderado

    def __init__(self):
        #inicializa o grafo vazio
        self.grafo = {}

    def adicionar_aresta(
        self,
        origem,
        destino,
        peso
    ):
        #adiciona uma aresta ao grafo

        if origem not in self.grafo:
            self.grafo[origem] = []

        if destino not in self.grafo:
            self.grafo[destino] = []

        self.grafo[origem].append(
            (peso, destino)
        )

        self.grafo[destino].append(
            (peso, origem)
        )

    def prim(self, inicio):
       #executa o algoritmo

        visitados = set()
        mst = []
        custo_total = 0

        fila_prioridade = [
            (0, inicio, None)
        ]

        while fila_prioridade:

            (
                peso,
                vertice_atual,
                origem
            ) = heapq.heappop(
                fila_prioridade
            )

            if vertice_atual in visitados:
                continue

            visitados.add(
                vertice_atual
            )

            if origem is not None:

                mst.append(
                    (
                        origem,
                        vertice_atual,
                        peso
                    )
                )

                custo_total += peso

            for (
                proximo_peso,
                vizinho
            ) in self.grafo[
                vertice_atual
            ]:

                if vizinho not in visitados:

                    heapq.heappush(
                        fila_prioridade,
                        (
                            proximo_peso,
                            vizinho,
                            vertice_atual
                        )
                    )

        return mst, custo_total


def main():
    #função principal

    grafo = Grafo()

    grafo.adicionar_aresta(
        "A",
        "B",
        2
    )

    grafo.adicionar_aresta(
        "A",
        "C",
        6
    )

    grafo.adicionar_aresta(
        "A",
        "D",
        3
    )

    grafo.adicionar_aresta(
        "B",
        "D",
        5
    )

    grafo.adicionar_aresta(
        "C",
        "D",
        4
    )

    mst, custo_total = grafo.prim("A")

    print(
        "Árvore Geradora Mínima:\n"
    )

    for (
        origem,
        destino,
        peso
    ) in mst:

        print(
            f"{origem} -> "
            f"{destino} | "
            f"Peso: {peso}"
        )

    print(
        f"\nCusto Total: "
        f"{custo_total}"
    )


if __name__ == "__main__":
    main()


"""

Árvore Geradora Mínima:

A -> B | Peso: 2
A -> D | Peso: 3
D -> C | Peso: 4

Custo Total: 9

"""
