# -*- coding: utf-8 -*-
"""
Algoritmos de Busca - Análise de Complexidade
==============================================

Este módulo demonstra e compara a complexidade de algoritmos de busca:
- Busca Linear: O(n)
- Busca Binária: O(log n)

Autor: Algoritmo Project
Data: 2025-10-21
"""

import time
import random
from typing import List, Tuple, Optional


def busca_linear(lista: List[int], alvo: int) -> Tuple[Optional[int], int]:
    """
    Busca Linear - Complexidade: O(n)

    Percorre a lista sequencialmente até encontrar o elemento ou chegar ao fim.

    Args:
        lista: Lista de inteiros
        alvo: Valor a ser buscado

    Returns:
        Tupla contendo (índice do elemento ou None, número de comparações)

    Complexidade de Tempo:
        - Melhor caso: O(1) - elemento está na primeira posição
        - Caso médio: O(n/2) ≈ O(n)
        - Pior caso: O(n) - elemento não existe ou está no final

    Complexidade de Espaço: O(1)
    """
    comparacoes = 0

    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == alvo:
            return i, comparacoes

    return None, comparacoes


def busca_binaria(lista: List[int], alvo: int) -> Tuple[Optional[int], int]:
    """
    Busca Binária - Complexidade: O(log n)

    Divide a lista ao meio repetidamente, eliminando metade das possibilidades
    a cada iteração. REQUER LISTA ORDENADA.

    Args:
        lista: Lista ordenada de inteiros
        alvo: Valor a ser buscado

    Returns:
        Tupla contendo (índice do elemento ou None, número de comparações)

    Complexidade de Tempo:
        - Melhor caso: O(1) - elemento está no meio
        - Caso médio: O(log n)
        - Pior caso: O(log n) - elemento não existe

    Complexidade de Espaço: O(1)
    """
    esquerda, direita = 0, len(lista) - 1
    comparacoes = 0

    while esquerda <= direita:
        comparacoes += 1
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return meio, comparacoes
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return None, comparacoes


def comparar_algoritmos(tamanho: int, num_testes: int = 10):
    """
    Compara o desempenho prático dos algoritmos de busca.

    Args:
        tamanho: Tamanho da lista a ser testada
        num_testes: Número de testes a realizar
    """
    print(f"\n{'='*70}")
    print(f"COMPARAÇÃO DE ALGORITMOS DE BUSCA - Tamanho: {tamanho:,} elementos")
    print(f"{'='*70}")

    # Criar lista ordenada
    lista = sorted(random.sample(range(tamanho * 10), tamanho))

    # Testar com elementos existentes
    elementos_teste = random.sample(lista, min(num_testes, len(lista)))

    comp_linear_total = 0
    comp_binaria_total = 0
    tempo_linear_total = 0
    tempo_binaria_total = 0

    for alvo in elementos_teste:
        # Busca Linear
        inicio = time.perf_counter()
        _, comp_linear = busca_linear(lista, alvo)
        tempo_linear = time.perf_counter() - inicio

        # Busca Binária
        inicio = time.perf_counter()
        _, comp_binaria = busca_binaria(lista, alvo)
        tempo_binaria = time.perf_counter() - inicio

        comp_linear_total += comp_linear
        comp_binaria_total += comp_binaria
        tempo_linear_total += tempo_linear
        tempo_binaria_total += tempo_binaria

    # Resultados médios
    print(f"\nResultados (média de {num_testes} buscas):")
    print(f"\n  Busca Linear [O(n)]:")
    print(f"    • Comparações médias: {comp_linear_total / num_testes:.2f}")
    print(f"    • Tempo médio: {tempo_linear_total / num_testes * 1e6:.4f} us")

    print(f"\n  Busca Binária [O(log n)]:")
    print(f"    • Comparações médias: {comp_binaria_total / num_testes:.2f}")
    print(f"    • Tempo médio: {tempo_binaria_total / num_testes * 1e6:.4f} us")

    print(f"\n  Ganho de Eficiência:")
    print(f"    • Redução de comparações: {comp_linear_total / comp_binaria_total:.2f}x")
    print(f"    • Aceleração de tempo: {tempo_linear_total / tempo_binaria_total:.2f}x")

    # Análise teórica
    import math
    comp_teorica_linear = tamanho / 2  # Caso médio
    comp_teorica_binaria = math.log2(tamanho)

    print(f"\n  Análise Teórica:")
    print(f"    • O(n) esperado: ~{comp_teorica_linear:.2f} comparações")
    print(f"    • O(log n) esperado: ~{comp_teorica_binaria:.2f} comparações")
    print(f"    • Diferença teórica: {comp_teorica_linear / comp_teorica_binaria:.2f}x")


def demonstrar_casos():
    """Demonstra casos específicos de uso dos algoritmos."""
    print("\n" + "="*70)
    print("DEMONSTRAÇÃO DE CASOS ESPECÍFICOS")
    print("="*70)

    lista = [3, 7, 12, 18, 23, 29, 34, 41, 50, 67]
    print(f"\nLista de teste: {lista}")

    # Caso 1: Elemento no início
    print("\n[Caso 1] Buscar elemento no início (3):")
    idx, comp = busca_linear(lista, 3)
    print(f"  Busca Linear: encontrado no índice {idx}, {comp} comparação(ões)")
    idx, comp = busca_binaria(lista, 3)
    print(f"  Busca Binária: encontrado no índice {idx}, {comp} comparação(ões)")

    # Caso 2: Elemento no meio
    print("\n[Caso 2] Buscar elemento no meio (23):")
    idx, comp = busca_linear(lista, 23)
    print(f"  Busca Linear: encontrado no índice {idx}, {comp} comparação(ões)")
    idx, comp = busca_binaria(lista, 23)
    print(f"  Busca Binária: encontrado no índice {idx}, {comp} comparação(ões)")

    # Caso 3: Elemento no final
    print("\n[Caso 3] Buscar elemento no final (67):")
    idx, comp = busca_linear(lista, 67)
    print(f"  Busca Linear: encontrado no índice {idx}, {comp} comparação(ões)")
    idx, comp = busca_binaria(lista, 67)
    print(f"  Busca Binária: encontrado no índice {idx}, {comp} comparação(ões)")

    # Caso 4: Elemento não existe
    print("\n[Caso 4] Buscar elemento inexistente (99):")
    idx, comp = busca_linear(lista, 99)
    print(f"  Busca Linear: {'não encontrado' if idx is None else f'encontrado no índice {idx}'}, {comp} comparação(ões)")
    idx, comp = busca_binaria(lista, 99)
    print(f"  Busca Binária: {'não encontrado' if idx is None else f'encontrado no índice {idx}'}, {comp} comparação(ões)")


if __name__ == "__main__":
    print("\n" + "="*70)
    print("ANÁLISE DE COMPLEXIDADE - ALGORITMOS DE BUSCA")
    print("="*70)

    # Demonstração com casos específicos
    demonstrar_casos()

    # Comparação com diferentes tamanhos
    tamanhos = [100, 1_000, 10_000, 100_000]

    for tamanho in tamanhos:
        comparar_algoritmos(tamanho, num_testes=10)

    print(f"\n{'='*70}")
    print("CONCLUSÃO:")
    print("="*70)
    print("""
A busca binária (O(log n)) é significativamente mais eficiente que a busca
linear (O(n)) para listas grandes, especialmente quando o elemento está no
meio ou final da lista. No entanto, requer que a lista esteja ordenada.

Para listas pequenas ou quando a ordenação é custosa, a busca linear pode
ser uma escolha razoável devido à sua simplicidade e menor overhead.
    """)
