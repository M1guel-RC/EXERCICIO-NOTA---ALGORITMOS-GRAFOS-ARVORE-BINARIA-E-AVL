from arvore_avl import AVLTree
from grafos import Graph


class City:
    """Representa uma cidade com seu grafo de bairros"""
    def __init__(self, name, city_id):
        self.name = name
        self.id = city_id
        self.district_graph = Graph()  # Grafo dos bairros da cidade

class NavigationSystem:
    """Sistema de navegação principal"""
    def __init__(self):
        self.cities = AVLTree()  # Árvore AVL de cidades (por ID)
        self.city_by_name = {}   # Dicionário para busca por nome
    
    def add_city(self, name, city_id):
        """Adiciona uma nova cidade ao sistema"""
        if city_id in self.city_by_name:
            print(f"Erro: Cidade com ID {city_id} já existe.")
            return
        
        city = City(name, city_id)
        self.cities.insert(city_id)
        self.city_by_name[city_id] = city
        print(f"Cidade '{name}' (ID: {city_id}) adicionada com sucesso.")
    
    def remove_city(self, city_id):
        """Remove uma cidade do sistema"""
        if city_id not in self.city_by_name:
            print(f"Erro: Cidade com ID {city_id} não encontrada.")
            return
        
        del self.city_by_name[city_id]
        self.cities.remove(city_id)
        print(f"Cidade (ID: {city_id}) removida com sucesso.")
    
    def show_cities_inorder(self):
        """Mostra cidades em ordem (in-order)"""
        cities = self.cities.inorder()
        if not cities:
            print("Nenhuma cidade cadastrada.")
            return
        
        print("\nCidades em ordem (por ID):")
        for city_id in cities:
            city = self.city_by_name[city_id]
            print(f"ID: {city_id}, Nome: {city.name}")
    
    def show_cities_preorder(self):
        """Mostra cidades em pré-ordem (pre-order)"""
        cities = self.cities.preorder()
        if not cities:
            print("Nenhuma cidade cadastrada.")
            return
        
        print("\nCidades em pré-ordem (por ID):")
        for city_id in cities:
            city = self.city_by_name[city_id]
            print(f"ID: {city_id}, Nome: {city.name}")
    
    def show_cities_postorder(self):
        """Mostra cidades em pós-ordem (post-order)"""
        cities = self.cities.postorder()
        if not cities:
            print("Nenhuma cidade cadastrada.")
            return
        
        print("\nCidades em pós-ordem (por ID):")
        for city_id in cities:
            city = self.city_by_name[city_id]
            print(f"ID: {city_id}, Nome: {city.name}")
    
    def add_district(self, city_id, district_name):
        """Adiciona um bairro a uma cidade"""
        if city_id not in self.city_by_name:
            print(f"Erro: Cidade com ID {city_id} não encontrada.")
            return
        
        city = self.city_by_name[city_id]
        city.district_graph.add_vertex(district_name)
        print(f"Bairro '{district_name}' adicionado à cidade {city.name}.")
    
    def add_road(self, city_id, district1, district2, weight=1):
        """Adiciona uma rua entre dois bairros"""
        if city_id not in self.city_by_name:
            print(f"Erro: Cidade com ID {city_id} não encontrada.")
            return
        
        city = self.city_by_name[city_id]
        city.district_graph.add_edge(district1, district2, weight)
        print(f"Rua adicionada entre '{district1}' e '{district2}' na cidade {city.name}.")
    
    def bfs_districts(self, city_id, start_district):
        """Executa BFS nos bairros de uma cidade"""
        if city_id not in self.city_by_name:
            print(f"Erro: Cidade com ID {city_id} não encontrada.")
            return
        
        city = self.city_by_name[city_id]
        if start_district not in city.district_graph.adj_list:
            print(f"Erro: Bairro '{start_district}' não encontrado na cidade {city.name}.")
            return
        
        order = city.district_graph.bfs(start_district)
        print("\nOrdem de visitação BFS:")
        print(" -> ".join(order))
    
    def dfs_districts(self, city_id, start_district):
        """Executa DFS nos bairros de uma cidade"""
        if city_id not in self.city_by_name:
            print(f"Erro: Cidade com ID {city_id} não encontrada.")
            return
        
        city = self.city_by_name[city_id]
        if start_district not in city.district_graph.adj_list:
            print(f"Erro: Bairro '{start_district}' não encontrado na cidade {city.name}.")
            return
        
        order = city.district_graph.dfs(start_district)
        print("\nOrdem de visitação DFS:")
        print(" -> ".join(order))
    
    def shortest_path_districts(self, city_id, start_district, end_district):
        """Encontra o caminho mínimo entre dois bairros"""
        if city_id not in self.city_by_name:
            print(f"Erro: Cidade com ID {city_id} não encontrada.")
            return
        
        city = self.city_by_name[city_id]
        if start_district not in city.district_graph.adj_list:
            print(f"Erro: Bairro '{start_district}' não encontrado na cidade {city.name}.")
            return
        
        if end_district not in city.district_graph.adj_list:
            print(f"Erro: Bairro '{end_district}' não encontrado na cidade {city.name}.")
            return
        
        path, distance = city.district_graph.shortest_path(start_district, end_district)
        
        if not path:
            print(f"\nNão há caminho entre '{start_district}' e '{end_district}'.")
        else:
            print(f"\nCaminho mais curto entre '{start_district}' e '{end_district}':")
            print(" -> ".join(path))
            print(f"Distância total: {distance}")

def main():
    """Função principal do sistema"""
    nav_system = NavigationSystem()
    
    while True:
        print("\n=== Sistema de Navegação de Rotas e Dados Hierárquicos ===")
        print("1. Adicionar cidade")
        print("2. Remover cidade")
        print("3. Mostrar cidades (em ordem)")
        print("4. Mostrar cidades (pré-ordem)")
        print("5. Mostrar cidades (pós-ordem)")
        print("6. Adicionar bairro a uma cidade")
        print("7. Adicionar rua entre bairros")
        print("8. Busca em Largura (BFS) nos bairros")
        print("9. Busca em Profundidade (DFS) nos bairros")
        print("10. Caminho mínimo entre bairros (Dijkstra)")
        print("0. Sair")
        
        option = input("\nEscolha uma opção: ")
        
        if option == "1":
            name = input("Nome da cidade: ")
            city_id = int(input("ID da cidade: "))
            nav_system.add_city(name, city_id)
        
        elif option == "2":
            city_id = int(input("ID da cidade a ser removida: "))
            nav_system.remove_city(city_id)
        
        elif option == "3":
            nav_system.show_cities_inorder()
        
        elif option == "4":
            nav_system.show_cities_preorder()
        
        elif option == "5":
            nav_system.show_cities_postorder()
        
        elif option == "6":
            city_id = int(input("ID da cidade: "))
            district_name = input("Nome do bairro: ")
            nav_system.add_district(city_id, district_name)
        
        elif option == "7":
            city_id = int(input("ID da cidade: "))
            district1 = input("Bairro 1: ")
            district2 = input("Bairro 2: ")
            weight = int(input("Distância (peso): "))
            nav_system.add_road(city_id, district1, district2, weight)
        
        elif option == "8":
            city_id = int(input("ID da cidade: "))
            start_district = input("Bairro inicial: ")
            nav_system.bfs_districts(city_id, start_district)
        
        elif option == "9":
            city_id = int(input("ID da cidade: "))
            start_district = input("Bairro inicial: ")
            nav_system.dfs_districts(city_id, start_district)
        
        elif option == "10":
            city_id = int(input("ID da cidade: "))
            start_district = input("Bairro inicial: ")
            end_district = input("Bairro final: ")
            nav_system.shortest_path_districts(city_id, start_district, end_district)
        
        elif option == "0":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()