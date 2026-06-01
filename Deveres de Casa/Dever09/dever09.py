# Dijkstra
import heapq

class Grafo:
    """Representa um grafo direcionado ponderado."""

    def __init__(self):
        """Inicializa o grafo."""
        self.grafo = {}

    def adicionar_aresta(
        self,
        origem,
        destino,
        peso
    ):
        """Adiciona uma aresta ao grafo."""

        if origem not in self.grafo:
            self.grafo[origem] = []

        if destino not in self.grafo:
            self.grafo[destino] = []

        self.grafo[origem].append(
            (destino, peso)
        )

    def dijkstra(
        self,
        origem,
        destino
    ):
        """Executa o algoritmo de Dijkstra."""

        distancias = {
            vertice: float("inf")
            for vertice in self.grafo
        }

        predecessores = {
            vertice: None
            for vertice in self.grafo
        }

        distancias[origem] = 0

        fila_prioridade = [
            (0, origem)
        ]

        while fila_prioridade:

            distancia_atual, vertice_atual = (
                heapq.heappop(
                    fila_prioridade
                )
            )

            for (
                vizinho,
                peso
            ) in self.grafo[
                vertice_atual
            ]:

                nova_distancia = (
                    distancia_atual + peso
                )

                if (
                    nova_distancia
                    < distancias[vizinho]
                ):

                    distancias[vizinho] = (
                        nova_distancia
                    )

                    predecessores[
                        vizinho
                    ] = vertice_atual

                    heapq.heappush(
                        fila_prioridade,
                        (
                            nova_distancia,
                            vizinho
                        )
                    )

        caminho = []
        atual = destino

        while atual is not None:
            caminho.append(atual)
            atual = predecessores[atual]

        caminho.reverse()

        return (
            caminho,
            distancias[destino]
        )


def main():
    """Função principal."""

    grafo = Grafo()

    grafo.adicionar_aresta(0, 1, 4)
    grafo.adicionar_aresta(0, 2, 1)
    grafo.adicionar_aresta(2, 1, 2)
    grafo.adicionar_aresta(1, 3, 1)
    grafo.adicionar_aresta(2, 4, 5)
    grafo.adicionar_aresta(3, 4, 1)

    caminho, custo = grafo.dijkstra(
        0,
        4
    )

    print(
        f"Caminho mínimo: "
        f"{caminho}"
    )

    print(
        f"Custo mínimo: "
        f"{custo}"
    )


if __name__ == "__main__":
    main()


"""
Caminho mínimo: [0, 2, 1, 3, 4]
Custo mínimo: 5
"""
