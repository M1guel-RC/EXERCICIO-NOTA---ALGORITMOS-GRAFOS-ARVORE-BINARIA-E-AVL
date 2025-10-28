# -*- coding: utf-8 -*-
"""
Exemplos de Complexidade de Algoritmos
========================================

Este módulo demonstra problemas práticos com diferentes complexidades:
- O(1): Tempo Constante
- O(n): Tempo Linear
- O(n²): Tempo Quadrático
- O(2^n): Tempo Exponencial
- O(n!): Tempo Fatorial

Autor: Algoritmo Project
Data: 2025-10-21
"""

import time
from typing import List, Dict, Set
import random


# ============================================================================
# O(1) - TEMPO CONSTANTE
# ============================================================================

def acesso_array(arr: List[int], indice: int) -> int:
    """
    Acesso direto a um elemento do array - O(1)

    Complexidade: O(1) - Tempo constante
    O tempo de execução não depende do tamanho do array.

    Args:
        arr: Lista de inteiros
        indice: Índice do elemento a acessar

    Returns:
        Elemento no índice especificado
    """
    return arr[indice]


def busca_hash(dicionario: Dict, chave: str):
    """
    Busca em dicionário/hash table - O(1) médio

    Complexidade: O(1) no caso médio
    Hash tables permitem acesso direto aos valores através das chaves.

    Args:
        dicionario: Dicionário Python
        chave: Chave a buscar

    Returns:
        Valor associado à chave ou None
    """
    return dicionario.get(chave)


def adicionar_conjunto(conjunto: Set, elemento):
    """
    Adição em conjunto - O(1) médio

    Complexidade: O(1) no caso médio
    Conjuntos usam hash tables para adicionar elementos rapidamente.

    Args:
        conjunto: Conjunto Python
        elemento: Elemento a adicionar
    """
    conjunto.add(elemento)


# ============================================================================
# O(n) - TEMPO LINEAR
# ============================================================================

def soma_elementos(arr: List[int]) -> int:
    """
    Soma de todos elementos - O(n)

    Complexidade: O(n)
    Percorre cada elemento uma vez.

    Args:
        arr: Lista de inteiros

    Returns:
        Soma de todos os elementos
    """
    soma = 0
    for num in arr:
        soma += num
    return soma


def encontrar_maximo(arr: List[int]) -> int:
    """
    Encontrar o maior elemento - O(n)

    Complexidade: O(n)
    Precisa verificar todos os elementos para garantir que encontrou o máximo.

    Args:
        arr: Lista de inteiros

    Returns:
        Maior elemento da lista
    """
    if not arr:
        raise ValueError("Lista vazia")

    maximo = arr[0]
    for num in arr[1:]:
        if num > maximo:
            maximo = num
    return maximo


def contar_pares(arr: List[int]) -> int:
    """
    Contar números pares - O(n)

    Complexidade: O(n)
    Percorre a lista uma vez contando elementos pares.

    Args:
        arr: Lista de inteiros

    Returns:
        Quantidade de números pares
    """
    contador = 0
    for num in arr:
        if num % 2 == 0:
            contador += 1
    return contador


# ============================================================================
# O(n²) - TEMPO QUADRÁTICO
# ============================================================================

def encontrar_duplicatas(arr: List[int]) -> List[tuple]:
    """
    Encontrar todos os pares de duplicatas - O(n²)

    Complexidade: O(n²)
    Compara cada elemento com todos os outros elementos.

    Args:
        arr: Lista de inteiros

    Returns:
        Lista de tuplas com pares duplicados
    """
    duplicatas = []
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                duplicatas.append((i, j, arr[i]))

    return duplicatas


def multiplicacao_matrizes(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    Multiplicação de matrizes - O(n³) para matrizes n×n

    Complexidade: O(n³) para matrizes quadradas
    Três loops aninhados para calcular cada elemento.

    Args:
        A: Matriz A
        B: Matriz B

    Returns:
        Matriz resultado A × B
    """
    linhas_A = len(A)
    colunas_A = len(A[0])
    colunas_B = len(B[0])

    # Inicializar matriz resultado com zeros
    resultado = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]

    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado


def bubble_sort_simples(arr: List[int]) -> List[int]:
    """
    Bubble Sort simples - O(n²)

    Complexidade: O(n²)
    Dois loops aninhados para comparar e trocar elementos.

    Args:
        arr: Lista de inteiros

    Returns:
        Lista ordenada
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ============================================================================
# O(2^n) - TEMPO EXPONENCIAL
# ============================================================================

def fibonacci_recursivo(n: int) -> int:
    """
    Fibonacci recursivo (ineficiente) - O(2^n)

    Complexidade: O(2^n)
    Cada chamada gera duas novas chamadas, criando uma árvore exponencial.

    Args:
        n: Posição da sequência de Fibonacci

    Returns:
        n-ésimo número de Fibonacci

    Nota: Esta é uma implementação didática. Na prática, use programação
    dinâmica ou iteração para calcular Fibonacci eficientemente.
    """
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def subconjuntos(arr: List[int]) -> List[List[int]]:
    """
    Gerar todos os subconjuntos - O(2^n)

    Complexidade: O(2^n)
    Um conjunto com n elementos tem 2^n subconjuntos possíveis.

    Args:
        arr: Lista de elementos

    Returns:
        Lista com todos os subconjuntos possíveis
    """
    resultado = [[]]

    for elemento in arr:
        # Para cada subconjunto existente, criar um novo com o elemento atual
        novos_subconjuntos = [subset + [elemento] for subset in resultado]
        resultado.extend(novos_subconjuntos)

    return resultado


# ============================================================================
# O(n!) - TEMPO FATORIAL
# ============================================================================

def permutacoes(arr: List[int]) -> List[List[int]]:
    """
    Gerar todas as permutações - O(n!)

    Complexidade: O(n!)
    Um conjunto com n elementos tem n! permutações possíveis.

    Args:
        arr: Lista de elementos

    Returns:
        Lista com todas as permutações
    """
    if len(arr) <= 1:
        return [arr]

    resultado = []

    for i in range(len(arr)):
        # Elemento atual
        atual = arr[i]
        # Restante (todos exceto o atual)
        restante = arr[:i] + arr[i + 1:]

        # Gerar permutações do restante
        for perm in permutacoes(restante):
            resultado.append([atual] + perm)

    return resultado


# ============================================================================
# DEMONSTRAÇÕES E COMPARAÇÕES
# ============================================================================

def demonstrar_o1():
    """Demonstra operações O(1)."""
    print("\n" + "="*70)
    print("O(1) - TEMPO CONSTANTE")
    print("="*70)

    arr = list(range(1_000_000))
    dicionario = {f"chave_{i}": i for i in range(1_000_000)}

    # Acesso a array
    inicio = time.perf_counter()
    valor = acesso_array(arr, 500_000)
    tempo = time.perf_counter() - inicio
    print(f"\n  Acesso a array (posição 500.000):")
    print(f"    • Valor: {valor}")
    print(f"    • Tempo: {tempo * 1e6:.4f} us")

    # Busca em hash
    inicio = time.perf_counter()
    valor = busca_hash(dicionario, "chave_500000")
    tempo = time.perf_counter() - inicio
    print(f"\n  Busca em dicionário (1.000.000 elementos):")
    print(f"    • Valor: {valor}")
    print(f"    • Tempo: {tempo * 1e6:.4f} us")

    print(f"\n  => O tempo é constante, independente do tamanho da estrutura!")


def demonstrar_on():
    """Demonstra operações O(n)."""
    print("\n" + "="*70)
    print("O(n) - TEMPO LINEAR")
    print("="*70)

    tamanhos = [1_000, 10_000, 100_000]

    for tamanho in tamanhos:
        arr = [random.randint(1, 1000) for _ in range(tamanho)]

        inicio = time.perf_counter()
        soma = soma_elementos(arr)
        tempo = time.perf_counter() - inicio

        print(f"\n  Soma de {tamanho:,} elementos:")
        print(f"    • Resultado: {soma:,}")
        print(f"    • Tempo: {tempo * 1000:.4f} ms")

    print(f"\n  => O tempo cresce proporcionalmente ao tamanho da entrada!")


def demonstrar_on2():
    """Demonstra operações O(n²)."""
    print("\n" + "="*70)
    print("O(n²) - TEMPO QUADRÁTICO")
    print("="*70)

    tamanhos = [100, 500, 1_000]

    for tamanho in tamanhos:
        arr = [random.randint(1, 100) for _ in range(tamanho)]

        inicio = time.perf_counter()
        duplicatas = encontrar_duplicatas(arr)
        tempo = time.perf_counter() - inicio

        print(f"\n  Buscar duplicatas em {tamanho} elementos:")
        print(f"    • Duplicatas encontradas: {len(duplicatas)}")
        print(f"    • Tempo: {tempo * 1000:.4f} ms")

    print(f"\n  => O tempo cresce quadraticamente! Dobrar n => quadruplica o tempo")


def demonstrar_exponencial():
    """Demonstra operações O(2^n)."""
    print("\n" + "="*70)
    print("O(2^n) - TEMPO EXPONENCIAL")
    print("="*70)

    print("\n  Fibonacci recursivo:")

    for n in range(5, 31, 5):
        inicio = time.perf_counter()
        resultado = fibonacci_recursivo(n)
        tempo = time.perf_counter() - inicio

        print(f"\n    fib({n}):")
        print(f"      • Resultado: {resultado:,}")
        print(f"      • Tempo: {tempo * 1000:.4f} ms")

        if tempo > 1:
            print(f"      [AVISO] Ficando muito lento!")
            break

    print(f"\n  => Crescimento exponencial! Impraticável para n > 40")


def demonstrar_fatorial():
    """Demonstra operações O(n!)."""
    print("\n" + "="*70)
    print("O(n!) - TEMPO FATORIAL")
    print("="*70)

    print("\n  Geração de permutações:")

    for n in range(3, 10):
        arr = list(range(n))

        inicio = time.perf_counter()
        perms = permutacoes(arr)
        tempo = time.perf_counter() - inicio

        import math
        esperado = math.factorial(n)

        print(f"\n    Permutações de {n} elementos:")
        print(f"      • Total de permutações: {len(perms):,} (esperado: {esperado:,})")
        print(f"      • Tempo: {tempo * 1000:.4f} ms")

        if tempo > 0.5:
            print(f"      [AVISO] Ficando muito lento!")
            break

    print(f"\n  => Crescimento fatorial! Extremamente impraticável para n > 12")


def comparacao_geral():
    """Comparação geral de todas as complexidades."""
    print("\n" + "="*70)
    print("COMPARAÇÃO GERAL DE COMPLEXIDADES")
    print("="*70)

    n_valores = [1, 10, 20, 30, 40, 50]

    print(f"\n  {'n':>5} | {'O(1)':>10} | {'O(log n)':>10} | {'O(n)':>10} | {'O(n²)':>12} | {'O(2^n)':>15} | {'O(n!)':>15}")
    print(f"  {'-'*6}|{'-'*12}|{'-'*12}|{'-'*12}|{'-'*14}|{'-'*17}|{'-'*17}")

    import math

    for n in n_valores:
        o_1 = 1
        o_log_n = math.log2(n) if n > 0 else 0
        o_n = n
        o_n2 = n ** 2
        o_2n = 2 ** n if n <= 30 else float('inf')
        o_nf = math.factorial(n) if n <= 20 else float('inf')

        def formatar(valor):
            if valor == float('inf'):
                return "> 10^15"
            elif valor > 1e12:
                return f"{valor:.2e}"
            elif valor > 1e6:
                return f"{valor/1e6:.2f}M"
            elif valor > 1e3:
                return f"{valor/1e3:.2f}K"
            else:
                return f"{valor:.0f}"

        print(f"  {n:5} | {formatar(o_1):>10} | {formatar(o_log_n):>10} | {formatar(o_n):>10} | {formatar(o_n2):>12} | {formatar(o_2n):>15} | {formatar(o_nf):>15}")


if __name__ == "__main__":
    print("\n" + "="*70)
    print("ANÁLISE DE COMPLEXIDADE - EXEMPLOS PRÁTICOS")
    print("="*70)

    # Demonstrações individuais
    demonstrar_o1()
    demonstrar_on()
    demonstrar_on2()
    demonstrar_exponencial()
    demonstrar_fatorial()

    # Comparação geral
    comparacao_geral()

    print(f"\n{'='*70}")
    print("RESUMO DAS COMPLEXIDADES:")
    print("="*70)
    print("""
EFICIENTES (Escaláveis):
  • O(1)      - Constante: Melhor possível, independente do tamanho
  • O(log n)  - Logarítmica: Muito eficiente (ex: busca binária)
  • O(n)      - Linear: Bom para a maioria dos casos
  • O(n log n)- Linearítmica: Ótimo para ordenação

ACEITÁVEIS (Uso limitado):
  • O(n²)     - Quadrática: Ok para datasets pequenos (<1000)
  • O(n³)     - Cúbica: Apenas para datasets muito pequenos

INEFICIENTES (Impraticáveis):
  • O(2^n)    - Exponencial: Apenas para n < 25
  • O(n!)     - Fatorial: Apenas para n < 12

REGRA DE OURO: Sempre prefira algoritmos com menor complexidade quando
trabalhar com grandes volumes de dados!
    """)
