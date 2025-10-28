from arvore_binaria import BinarySearchTree, Node

class AVLNode(Node):
    """Nó para árvore AVL com informação de altura"""
    def __init__(self, key):
        super().__init__(key)
        self.height = 1

class AVLTree(BinarySearchTree):
    """Implementação de Árvore AVL com balanceamento automático"""
    def __init__(self):
        super().__init__()
    
    def insert(self, key):
        """
        Insere um novo nó na árvore AVL e realiza balanceamento.
        Complexidade: O(log n), devido ao balanceamento automático.
        """
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        # 1. Inserção padrão de BST
        if node is None:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # Chaves duplicadas não são permitidas
        
        # 2. Atualizar altura do nó ancestral
        node.height = 1 + max(self._get_height(node.left), 
                              self._get_height(node.right))
        
        # 3. Obter fator de balanceamento
        balance = self._get_balance(node)
        
        # 4. Casos de desbalanceamento
        
        # Caso LL - Rotação simples à direita
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        
        # Caso RR - Rotação simples à esquerda
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        
        # Caso LR - Rotação dupla esquerda-direita
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        # Caso RL - Rotação dupla direita-esquerda
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node
    
    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        
        # Realizar rotação
        y.left = z
        z.right = T2
        
        # Atualizar alturas
        z.height = 1 + max(self._get_height(z.left), 
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), 
                           self._get_height(y.right))
        
        return y
    
    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        
        # Realizar rotação
        y.right = z
        z.left = T3
        
        # Atualizar alturas
        z.height = 1 + max(self._get_height(z.left), 
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), 
                           self._get_height(y.right))
        
        return y
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def remove(self, key):
        """
        Remove um nó da árvore AVL e realiza balanceamento.
        Complexidade: O(log n), devido ao balanceamento automático.
        """
        self.root = self._remove(self.root, key)
    
    def _remove(self, node, key):
        # 1. Remoção padrão de BST
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            # Nó com apenas um filho ou sem filhos
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Nó com dois filhos: obter o sucessor in-order
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._remove(node.right, temp.key)
        
        # Se a árvore tinha apenas um nó, retornar
        if node is None:
            return node
        
        # 2. Atualizar altura do nó ancestral
        node.height = 1 + max(self._get_height(node.left), 
                              self._get_height(node.right))
        
        # 3. Obter fator de balanceamento
        balance = self._get_balance(node)
        
        # 4. Casos de desbalanceamento
        
        # Caso LL
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        
        # Caso RR
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        
        # Caso LR
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        # Caso RL
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node