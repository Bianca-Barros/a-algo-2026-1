import heapq

class Paciente:
    """representa um paciente"""

    def __init__(self, nome: str, nivel_dor: int):
        self.nome = nome
        self.nivel_dor = nivel_dor

    def __lt__(self, other):
        return self.nivel_dor > other.nivel_dor

    def __repr__(self):
        return f"{self.nome} (Dor: {self.nivel_dor})"


class TriagemHospitalar:
    """sistema de triagem com max-heap"""

    def __init__(self):
        self.heap = []

    def adicionar_paciente(self, nome: str, nivel_dor: int):
        paciente = Paciente(nome, nivel_dor)
        heapq.heappush(self.heap, paciente)

        print(f"Paciente {nome} adicionado.")

    def atender_paciente(self):
        if not self.heap:
            print("Fila vazia.")
            return None

        paciente = heapq.heappop(self.heap)

        print(f"Atendendo: {paciente}")

        return paciente

    def alterar_prioridade(self, nome: str, novo_nivel: int):
        for paciente in self.heap:
            if paciente.nome == nome:
                print(
                    f"Prioridade alterada: "
                    f"{paciente.nivel_dor} -> {novo_nivel}"
                )

                paciente.nivel_dor = novo_nivel
                heapq.heapify(self.heap)

                return

        print("Paciente não encontrado.")

    def mostrar_fila(self):
        if not self.heap:
            print("Fila vazia.")
            return

        print("\nFila de Atendimento:")

        for paciente in sorted(
            self.heap,
            key=lambda p: p.nivel_dor,
            reverse=True
        ):
            print(paciente)


def analisar_complexidade():
    """exibe as complexidades"""

    print("\nComplexidades:")
    print("Inserção: O(log N)")
    print("Remoção: O(log N)")
    print("Alterar prioridade: O(N)")
    print("Exibição ordenada: O(N log N)")


def main():
    sistema = TriagemHospitalar()

    sistema.adicionar_paciente("Carlos", 5)
    sistema.adicionar_paciente("Ana", 9)
    sistema.adicionar_paciente("Marina", 7)
    sistema.adicionar_paciente("João", 3)

    sistema.mostrar_fila()

    sistema.atender_paciente()

    sistema.alterar_prioridade("João", 10)

    sistema.mostrar_fila()

    analisar_complexidade()


if __name__ == "__main__":
    main()

"""
Paciente Carlos adicionado.
Paciente Ana adicionado.
Paciente Marina adicionado.
Paciente João adicionado.

Fila de Atendimento:
Ana (Dor: 9)
Marina (Dor: 7)
Carlos (Dor: 5)
João (Dor: 3)
Atendendo: Ana (Dor: 9)
Prioridade alterada: 3 -> 10

Fila de Atendimento:
João (Dor: 10)
Marina (Dor: 7)
Carlos (Dor: 5)

Complexidades:
Inserção: O(log N)
Remoção: O(log N)
Alterar prioridade: O(N)
Exibição ordenada: O(N log N)
"""
