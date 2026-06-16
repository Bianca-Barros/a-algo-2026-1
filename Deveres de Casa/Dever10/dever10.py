# kruskal
class UnionFind:
    """Implementa a estrutura Union-Find."""

    def __init__(self, quantidade_vertices):
        """Inicializa os conjuntos."""

        self.pai = list(
            range(quantidade_vertices)
        )

        self.rank = [
            0
            for _ in range(
                quantidade_vertices
            )
        ]

    def find(self, vertice):
        """Retorna o representante do conjunto."""

        if self.pai[vertice] != vertice:

            self.pai[vertice] = self.find(
                self.pai[vertice]
            )

        return self.pai[vertice]

    def union(
        self,
        origem,
        destino
    ):
        """Une dois conjuntos."""

        raiz_origem = self.find(origem)
        raiz_destino = self.find(destino)

        if raiz_origem == raiz_destino:
            return False

        if (
            self.rank[raiz_origem]
            < self.rank[raiz_destino]
        ):

            self.pai[
                raiz_origem
            ] = raiz_destino

        elif (
            self.rank[raiz_origem]
            > self.rank[raiz_destino]
        ):

            self.pai[
                raiz_destino
            ] = raiz_origem

        else:

            self.pai[
                raiz_destino
            ] = raiz_origem

            self.rank[
                raiz_origem
            ] += 1

        return True


class Grafo:
    """Representa um grafo não direcionado."""

    def __init__(
        self,
        quantidade_vertices
    ):
        """Inicializa o grafo."""

        self.quantidade_vertices = (
            quantidade_vertices
        )

        self.arestas = []

    def adicionar_aresta(
        self,
        origem,
        destino
    ):
        """Adiciona uma aresta."""

        self.arestas.append(
            (
                origem,
                destino
            )
        )

    def tem_ciclo(self):
        """Verifica se existe ciclo."""

        conjuntos = UnionFind(
            self.quantidade_vertices
        )

        for (
            origem,
            destino
        ) in self.arestas:

            if not conjuntos.union(
                origem,
                destino
            ):

                return True

        return False


def main():
    """Função principal."""

    grafo = Grafo(5)

    grafo.adicionar_aresta(
        0,
        1
    )

    grafo.adicionar_aresta(
        1,
        2
    )

    grafo.adicionar_aresta(
        2,
        3
    )

    grafo.adicionar_aresta(
        3,
        4
    )

    grafo.adicionar_aresta(
        4,
        1
    )

    if grafo.tem_ciclo():

        print(
            "O grafo possui ciclo."
        )

    else:

        print(
            "O grafo não possui ciclo."a
        )


if __name__ == "__main__":
    main()

"""
O grafo possui ciclo.
"""
