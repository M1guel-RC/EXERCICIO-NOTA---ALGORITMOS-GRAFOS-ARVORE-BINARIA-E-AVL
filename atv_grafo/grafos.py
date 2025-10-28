import heapq
from collections import deque

class Graph:
    """Implementação de Grafo usando lista de adjacência"""
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {}
    
    def add_vertex(self, vertex):
        """Adiciona um vértice ao grafo"""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, u, v, weight=1):
        """
        Adiciona uma aresta ao grafo.
        Complexidade: O(1) para listas de adjacência.
        """
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append((v, weight))
        if not self.directed:
            self.adj_list[v].append((u, weight))
    
    def bfs(self, start):
        """
        Busca em Largura (BFS).
        Complexidade: O(V + E), onde V é o número de vértices e E é o número de arestas.
        """
        visited = set()
        queue = deque()
        queue.append(start)
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor, _ in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """
        Busca em Profundidade (DFS).
        Complexidade: O(V + E), onde V é o número de vértices e E é o número de arestas.
        """
        visited = set()
        stack = [start]
        visited.add(start)
        result = []
        
        while stack:
            vertex = stack.pop()
            result.append(vertex)
            
            for neighbor, _ in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        return result
    
    def dijkstra(self, start):
        """
        Algoritmo de Dijkstra para caminho mínimo.
        Complexidade: O(E log V) usando um heap binário.
        """
        distances = {vertex: float('infinity') for vertex in self.adj_list}
        predecessors = {vertex: None for vertex in self.adj_list}
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Se encontramos um caminho mais curto, ignoramos
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.adj_list.get(current_vertex, []):
                distance = current_distance + weight
                
                # Se encontramos um caminho mais curto para o vizinho
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances, predecessors
    
    def shortest_path(self, start, end):
        """Retorna o caminho mínimo entre dois vértices usando Dijkstra"""
        distances, predecessors = self.dijkstra(start)
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            current = predecessors[current]
        
        path.reverse()
        
        if path[0] == start:
            return path, distances[end]
        else:
            return [], float('infinity')  # Não há caminho