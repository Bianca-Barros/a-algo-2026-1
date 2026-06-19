#busca estocastica
import math
import random


class SimulatedAnnealing:
    """Implementa Simulated Annealing para o problema das N-Rainhas."""

    def __init__(
        self,
        tamanho,
        temperatura_inicial=1000,
        temperatura_final=0.001,
        fator_resfriamento=0.995
    ):
        """Inicializa os parâmetros do algoritmo."""

        self.tamanho = tamanho
        self.temperatura_inicial = temperatura_inicial
        self.temperatura_final = temperatura_final
        self.fator_resfriamento = fator_resfriamento

    def calcular_conflitos(self, tabuleiro):
        """Retorna o número de conflitos do tabuleiro."""

        conflitos = 0

        for i in range(self.tamanho):
            for j in range(i + 1, self.tamanho):

                mesma_linha = (
                    tabuleiro[i] == tabuleiro[j]
                )

                mesma_diagonal = (
                    abs(tabuleiro[i] - tabuleiro[j])
                    == abs(i - j)
                )

                if mesma_linha or mesma_diagonal:
                    conflitos += 1

        return conflitos

    def gerar_vizinho(self, tabuleiro):
        """Gera um estado vizinho aleatório."""

        vizinho = tabuleiro.copy()

        coluna = random.randint(
            0,
            self.tamanho - 1
        )

        linha = random.randint(
            0,
            self.tamanho - 1
        )

        vizinho[coluna] = linha

        return vizinho

    def executar(self):
        """Executa o algoritmo Simulated Annealing."""

        estado_atual = [
            random.randint(
                0,
                self.tamanho - 1
            )
            for _ in range(self.tamanho)
        ]

        custo_atual = self.calcular_conflitos(
            estado_atual
        )

        temperatura = self.temperatura_inicial

        historico = []

        while (
            temperatura > self.temperatura_final
            and custo_atual > 0
        ):

            vizinho = self.gerar_vizinho(
                estado_atual
            )

            custo_vizinho = (
                self.calcular_conflitos(
                    vizinho
                )
            )

            delta = (
                custo_vizinho - custo_atual
            )

            if delta < 0:

                estado_atual = vizinho
                custo_atual = custo_vizinho

            else:

                probabilidade = math.exp(
                    -delta / temperatura
                )

                if random.random() < probabilidade:

                    estado_atual = vizinho
                    custo_atual = custo_vizinho

            historico.append(
                custo_atual
            )

            temperatura *= (
                self.fator_resfriamento
            )

        return (
            estado_atual,
            custo_atual,
            historico
        )


def main():
    """Executa o algoritmo para 12 rainhas."""

    sa = SimulatedAnnealing(
        tamanho=12
    )

    solucao, conflitos, historico = (
        sa.executar()
    )

    print("Solução encontrada:")
    print(solucao)

    print(
        f"Número de conflitos: "
        f"{conflitos}"
    )


if __name__ == "__main__":
    main()

"""
Solução encontrada:
[3, 8, 11, 4, 6, 1, 10, 7, 0, 2, 5, 9]
Número de conflitos: 0
"""
