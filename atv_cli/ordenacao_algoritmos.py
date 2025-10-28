# -*- coding: utf-8 -*-
"""
Algoritmos de Ordenação - Análise de Complexidade
==================================================

Este módulo demonstra e compara a complexidade de algoritmos de ordenação:
- Bubble Sort: O(n²)
- Selection Sort: O(n²)
- Merge Sort: O(n log n)
- Quick Sort: O(n log n) médio, O(n²) pior caso

Autor: Algoritmo Project
Data: 2025-10-21
"""

import time
import random
from typing import List, Tuple
import copy


def bubble_sort(lista: List[int]) -> Tuple[List[int], int]:
    """
    Bubble Sort - Complexidade: O(n²)

    Compara elementos adjacentes e os troca se estiverem fora de ordem.
    O processo se repete até que nenhuma troca seja necessária.

    Args:
        lista: Lista de inteiros a ser ordenada

    Returns:
        Tupla contendo (lista ordenada, número de comparações)

    Complexidade de Tempo:
        - Melhor caso: O(n) - lista já ordenada (com otimização)
        - Caso médio: O(n²)
        - Pior caso: O(n²) - lista ordenada inversamente

    Complexidade de Espaço: O(1) - ordenação in-place
    """
    arr = lista.copy()
    n = len(arr)
    comparacoes = 0

    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True

        # Otimização: se não houve troca, a lista está ordenada
        if not trocou:
            break

    return arr, comparacoes


def selection_sort(lista: List[int]) -> Tuple[List[int], int]:
    """
    Selection Sort - Complexidade: O(n²)

    Encontra o menor elemento e o coloca na primeira posição,
    depois encontra o segundo menor e o coloca na segunda posição, e assim por diante.

    Args:
        lista: Lista de inteiros a ser ordenada

    Returns:
        Tupla contendo (lista ordenada, número de comparações)

    Complexidade de Tempo:
        - Melhor caso: O(n²)
        - Caso médio: O(n²)
        - Pior caso: O(n²)

    Complexidade de Espaço: O(1) - ordenação in-place
    """
    arr = lista.copy()
    n = len(arr)
    comparacoes = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr, comparacoes


def merge_sort(lista: List[int]) -> Tuple[List[int], int]:
    """
    Merge Sort - Complexidade: O(n log n)

    Algoritmo de divisão e conquista que divide a lista ao meio recursivamente,
    ordena cada metade e depois mescla as metades ordenadas.

    Args:
        lista: Lista de inteiros a ser ordenada

    Returns:
        Tupla contendo (lista ordenada, número de comparações)

    Complexidade de Tempo:
        - Melhor caso: O(n log n)
        - Caso médio: O(n log n)
        - Pior caso: O(n log n)

    Complexidade de Espaço: O(n) - requer espaço auxiliar
    """
    comparacoes = [0]  # Usar lista para permitir modificação na recursão

    def merge(esquerda: List[int], direita: List[int]) -> List[int]:
        resultado = []
        i = j = 0

        while i < len(esquerda) and j < len(direita):
            comparacoes[0] += 1
            if esquerda[i] <= direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1

        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado

    def merge_sort_recursivo(arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        meio = len(arr) // 2
        esquerda = merge_sort_recursivo(arr[:meio])
        direita = merge_sort_recursivo(arr[meio:])

        return merge(esquerda, direita)

    resultado = merge_sort_recursivo(lista)
    return resultado, comparacoes[0]


def quick_sort(lista: List[int]) -> Tuple[List[int], int]:
    """
    Quick Sort - Complexidade: O(n log n) médio

    Algoritmo de divisão e conquista que escolhe um pivô e particiona a lista
    em elementos menores e maiores que o pivô.

    Args:
        lista: Lista de inteiros a ser ordenada

    Returns:
        Tupla contendo (lista ordenada, número de comparações)

    Complexidade de Tempo:
        - Melhor caso: O(n log n)
        - Caso médio: O(n log n)
        - Pior caso: O(n²) - quando o pivô é sempre o menor/maior elemento

    Complexidade de Espaço: O(log n) - devido à pilha de recursão
    """
    arr = lista.copy()
    comparacoes = [0]

    def particionar(arr: List[int], baixo: int, alto: int) -> int:
        # Escolher pivô usando mediana de três para evitar pior caso
        meio = (baixo + alto) // 2

        # Ordenar baixo, meio e alto para escolher mediana
        if arr[baixo] > arr[meio]:
            arr[baixo], arr[meio] = arr[meio], arr[baixo]
        if arr[baixo] > arr[alto]:
            arr[baixo], arr[alto] = arr[alto], arr[baixo]
        if arr[meio] > arr[alto]:
            arr[meio], arr[alto] = arr[alto], arr[meio]

        # Colocar mediana no penúltimo lugar
        arr[meio], arr[alto - 1] = arr[alto - 1], arr[meio]
        pivo = arr[alto - 1]

        i = baixo
        j = alto - 1

        while True:
            i += 1
            while arr[i] < pivo:
                comparacoes[0] += 1
                i += 1

            j -= 1
            while arr[j] > pivo:
                comparacoes[0] += 1
                j -= 1

            comparacoes[0] += 2

            if i >= j:
                break

            arr[i], arr[j] = arr[j], arr[i]

        arr[i], arr[alto - 1] = arr[alto - 1], arr[i]
        return i

    def quick_sort_recursivo(arr: List[int], baixo: int, alto: int):
        # Usar insertion sort para listas pequenas
        if alto - baixo < 10:
            for i in range(baixo + 1, alto + 1):
                key = arr[i]
                j = i - 1
                while j >= baixo and arr[j] > key:
                    comparacoes[0] += 1
                    arr[j + 1] = arr[j]
                    j -= 1
                if j >= baixo:
                    comparacoes[0] += 1
                arr[j + 1] = key
            return

        if baixo < alto:
            pi = particionar(arr, baixo, alto)
            quick_sort_recursivo(arr, baixo, pi - 1)
            quick_sort_recursivo(arr, pi + 1, alto)

    if len(arr) > 0:
        quick_sort_recursivo(arr, 0, len(arr) - 1)
    return arr, comparacoes[0]


def comparar_algoritmos(tamanho: int, tipo_lista: str = "aleatoria"):
    """
    Compara o desempenho dos algoritmos de ordenação.

    Args:
        tamanho: Tamanho da lista a ser testada
        tipo_lista: Tipo de lista ("aleatoria", "ordenada", "reversa")
    """
    print(f"\n{'='*70}")
    print(f"COMPARAÇÃO - Tamanho: {tamanho:,} | Tipo: {tipo_lista.upper()}")
    print(f"{'='*70}")

    # Gerar lista de teste
    if tipo_lista == "aleatoria":
        lista = [random.randint(1, tamanho * 10) for _ in range(tamanho)]
    elif tipo_lista == "ordenada":
        lista = list(range(tamanho))
    elif tipo_lista == "reversa":
        lista = list(range(tamanho, 0, -1))
    else:
        lista = [random.randint(1, tamanho * 10) for _ in range(tamanho)]

    algoritmos = [
        ("Bubble Sort [O(n²)]", bubble_sort),
        ("Selection Sort [O(n²)]", selection_sort),
        ("Merge Sort [O(n log n)]", merge_sort),
        ("Quick Sort [O(n log n)]", quick_sort),
    ]

    resultados = []

    for nome, funcao in algoritmos:
        # Pular algoritmos O(n²) para listas muito grandes
        if tamanho > 10000 and "O(n²)" in nome:
            print(f"\n  {nome}: [PULADO - muito lento para {tamanho:,} elementos]")
            continue

        inicio = time.perf_counter()
        lista_ordenada, comparacoes = funcao(lista)
        tempo = time.perf_counter() - inicio

        # Verificar se está ordenado
        assert lista_ordenada == sorted(lista), f"{nome} falhou na ordenação!"

        resultados.append((nome, comparacoes, tempo))

        print(f"\n  {nome}:")
        print(f"    • Comparações: {comparacoes:,}")
        print(f"    • Tempo: {tempo * 1000:.4f} ms")

    # Análise comparativa
    if len(resultados) > 1:
        print(f"\n  Análise Comparativa:")
        mais_rapido = min(resultados, key=lambda x: x[2])
        print(f"    • Algoritmo mais rápido: {mais_rapido[0]}")

        for nome, comp, tempo in resultados:
            if nome != mais_rapido[0]:
                aceleracao = tempo / mais_rapido[2]
                print(f"    • {nome} é {aceleracao:.2f}x mais lento")


def demonstrar_casos():
    """Demonstra casos específicos com listas pequenas."""
    print("\n" + "="*70)
    print("DEMONSTRAÇÃO COM LISTAS PEQUENAS")
    print("="*70)

    lista_teste = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
    print(f"\nLista original: {lista_teste}")

    algoritmos = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
    ]

    for nome, funcao in algoritmos:
        resultado, comp = funcao(lista_teste)
        print(f"\n  {nome}:")
        print(f"    Resultado: {resultado}")
        print(f"    Comparações: {comp}")


def analisar_pior_caso():
    """Analisa o comportamento no pior caso para Quick Sort."""
    print("\n" + "="*70)
    print("ANÁLISE DO PIOR CASO - QUICK SORT")
    print("="*70)

    tamanho = 1000

    # Melhor caso: lista aleatória
    lista_aleatoria = [random.randint(1, tamanho * 10) for _ in range(tamanho)]
    inicio = time.perf_counter()
    _, comp_aleatoria = quick_sort(lista_aleatoria)
    tempo_aleatoria = time.perf_counter() - inicio

    # Pior caso: lista já ordenada (pode causar O(n²) com pivô fixo)
    lista_ordenada = list(range(tamanho))
    inicio = time.perf_counter()
    _, comp_ordenada = quick_sort(lista_ordenada)
    tempo_ordenada = time.perf_counter() - inicio

    print(f"\n  Lista Aleatória (caso médio):")
    print(f"    • Comparações: {comp_aleatoria:,}")
    print(f"    • Tempo: {tempo_aleatoria * 1000:.4f} ms")

    print(f"\n  Lista Ordenada (pior caso potencial):")
    print(f"    • Comparações: {comp_ordenada:,}")
    print(f"    • Tempo: {tempo_ordenada * 1000:.4f} ms")

    print(f"\n  Diferença: {comp_ordenada / comp_aleatoria:.2f}x mais comparações no pior caso")


if __name__ == "__main__":
    print("\n" + "="*70)
    print("ANÁLISE DE COMPLEXIDADE - ALGORITMOS DE ORDENAÇÃO")
    print("="*70)

    # Demonstração com listas pequenas
    demonstrar_casos()

    # Comparação com diferentes tamanhos e tipos
    tamanhos = [100, 1_000, 10_000]

    for tamanho in tamanhos:
        comparar_algoritmos(tamanho, "aleatoria")

    # Análise de melhor e pior caso
    print("\n" + "="*70)
    print("ANÁLISE DE CASOS ESPECIAIS")
    print("="*70)

    comparar_algoritmos(1000, "ordenada")
    comparar_algoritmos(1000, "reversa")

    # Análise do pior caso do Quick Sort
    analisar_pior_caso()

    print(f"\n{'='*70}")
    print("CONCLUSÃO:")
    print("="*70)
    print("""
Algoritmos O(n²) como Bubble Sort e Selection Sort são simples mas ineficientes
para grandes volumes de dados. São adequados apenas para listas pequenas.

Algoritmos O(n log n) como Merge Sort e Quick Sort são muito mais eficientes
para grandes datasets:
- Merge Sort: consistente O(n log n) em todos os casos, mas usa mais memória
- Quick Sort: mais rápido na prática, mas pode degradar para O(n²) no pior caso

Para listas grandes (>1000 elementos), sempre prefira algoritmos O(n log n).
    """)
