# Análise de Complexidade de Algoritmos em Python

Este repositório contém 3 códigos Python que demonstram e analisam diferentes complexidades algorítmicas, com exemplos práticos, testes e comparações de desempenho.

## 📋 Descrição

Projeto desenvolvido para demonstrar os princípios de complexidade em algoritmos, incluindo notação Big O e análise de desempenho prático. Cada código foi testado e documentado para facilitar o entendimento dos conceitos.

## 🎯 Códigos Desenvolvidos

### 1. `busca_algoritmos.py` - Algoritmos de Busca

Demonstra e compara a complexidade de algoritmos de busca:

- **Busca Linear**: O(n)
- **Busca Binária**: O(log n)

**Funcionalidades:**
- Implementação com contagem de comparações
- Comparação de desempenho com diferentes tamanhos de dados
- Demonstração de casos específicos (início, meio, fim, elemento inexistente)
- Análise teórica vs prática

**Como executar:**
```bash
python busca_algoritmos.py
```

**Principais conclusões:**
- Busca binária é significativamente mais eficiente (até 3000x menos comparações)
- Requer lista ordenada
- Para listas pequenas, busca linear pode ser adequada pela simplicidade

---

### 2. `ordenacao_algoritmos.py` - Algoritmos de Ordenação

Demonstra e compara diferentes algoritmos de ordenação:

- **Bubble Sort**: O(n²)
- **Selection Sort**: O(n²)
- **Merge Sort**: O(n log n)
- **Quick Sort**: O(n log n) médio, O(n²) pior caso

**Funcionalidades:**
- Implementação de 4 algoritmos clássicos
- Comparação com listas aleatórias, ordenadas e reversas
- Análise de melhor, médio e pior caso
- Otimizações no Quick Sort (mediana de três + insertion sort para listas pequenas)

**Como executar:**
```bash
python ordenacao_algoritmos.py
```

**Principais conclusões:**
- Algoritmos O(n²) são impraticáveis para listas grandes (>10.000 elementos)
- Merge Sort tem desempenho consistente O(n log n)
- Quick Sort é mais rápido na prática, mas pode degradar
- Para listas grandes, sempre use O(n log n)

---

### 3. `complexidade_exemplos.py` - Exemplos Práticos de Complexidades

Demonstra problemas práticos com diferentes complexidades:

- **O(1)**: Tempo Constante (acesso a array, busca em hash)
- **O(n)**: Tempo Linear (soma, busca de máximo)
- **O(n²)**: Tempo Quadrático (encontrar duplicatas, multiplicação de matrizes)
- **O(2^n)**: Tempo Exponencial (Fibonacci recursivo, subconjuntos)
- **O(n!)**: Tempo Fatorial (permutações)

**Funcionalidades:**
- Implementações didáticas de cada complexidade
- Demonstrações práticas com medição de tempo
- Comparação visual de crescimento das complexidades
- Tabela comparativa mostrando o crescimento de cada notação

**Como executar:**
```bash
python complexidade_exemplos.py
```

**Principais conclusões:**
- O(1), O(log n), O(n) e O(n log n) são eficientes e escaláveis
- O(n²) é aceitável apenas para datasets pequenos
- O(2^n) e O(n!) são impraticáveis para n > 30

---

## 📊 Resumo das Complexidades

### Eficientes (Escaláveis)
- **O(1)** - Constante: Melhor possível, independente do tamanho
- **O(log n)** - Logarítmica: Muito eficiente (ex: busca binária)
- **O(n)** - Linear: Bom para a maioria dos casos
- **O(n log n)** - Linearítmica: Ótimo para ordenação

### Aceitáveis (Uso Limitado)
- **O(n²)** - Quadrática: Ok para datasets pequenos (<1000)
- **O(n³)** - Cúbica: Apenas para datasets muito pequenos

### Ineficientes (Impraticáveis)
- **O(2^n)** - Exponencial: Apenas para n < 25
- **O(n!)** - Fatorial: Apenas para n < 12

---

## 🔧 Requisitos

- Python 3.7 ou superior
- Bibliotecas padrão: `time`, `random`, `typing`, `math`

Não há dependências externas!

---

## 🚀 Como Usar

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd atv_cli
```

2. Execute qualquer um dos scripts:
```bash
python busca_algoritmos.py
python ordenacao_algoritmos.py
python complexidade_exemplos.py
```

3. Analise os resultados no console

---

## 📈 Resultados dos Testes

### Busca (100.000 elementos)
- **Busca Linear**: ~50.000 comparações
- **Busca Binária**: ~17 comparações
- **Ganho**: ~3000x mais eficiente

### Ordenação (10.000 elementos)
- **Bubble Sort**: ~50.000.000 comparações, 7.2s
- **Quick Sort**: ~156.000 comparações, 0.03s
- **Ganho**: ~240x mais rápido

### Complexidades
| n   | O(1) | O(log n) | O(n)  | O(n²)    | O(2^n)      | O(n!)       |
|-----|------|----------|-------|----------|-------------|-------------|
| 10  | 1    | 3        | 10    | 100      | 1.024       | 3.628.800   |
| 20  | 1    | 4        | 20    | 400      | 1.048.576   | 2.43 × 10¹⁸ |
| 30  | 1    | 5        | 30    | 900      | 1.073.741.824 | > 10³²    |

---

## 📚 Conceitos Abordados

1. **Notação Big O**: Análise assintótica de algoritmos
2. **Melhor, Médio e Pior Caso**: Diferentes cenários de execução
3. **Complexidade de Tempo vs Espaço**: Trade-offs entre velocidade e memória
4. **Otimizações**: Técnicas para melhorar algoritmos (mediana de três, insertion sort híbrido)
5. **Análise Empírica**: Medição real de desempenho

---

## 🎓 Objetivos Educacionais

Este projeto demonstra:
- Como diferentes algoritmos escalam com o tamanho da entrada
- A importância de escolher o algoritmo correto para cada problema
- Como medir e analisar o desempenho de algoritmos
- A diferença entre análise teórica e desempenho prático

---

## 📝 Documentação do Código

Todos os códigos incluem:
- **Docstrings detalhadas** para cada função
- **Análise de complexidade** (tempo e espaço)
- **Comentários explicativos** no código
- **Type hints** para clareza
- **Exemplos de uso** na seção `if __name__ == "__main__"`

---

## 🤝 Contribuições

Este é um projeto educacional. Sugestões e melhorias são bem-vindas!

---

## 👨‍💻 Autor

**Algoritmo Project**
Data: 2025-10-21

---

## 📖 Referências

- Introduction to Algorithms (CLRS)
- The Algorithm Design Manual (Skiena)
- Python Time Complexity: https://wiki.python.org/moin/TimeComplexity

---

## ⚡ Regra de Ouro

**Sempre prefira algoritmos com menor complexidade quando trabalhar com grandes volumes de dados!**

Para pequenos datasets, a simplicidade do código pode ser mais importante que a eficiência algorítmica.
