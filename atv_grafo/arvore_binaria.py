class Node:
    """Nó básico para árvore binária"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """Implementação de Árvore Binária de Busca (BST)"""
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """
        Insere um novo nó na árvore.
        Complexidade: O(h), onde h é a altura da árvore.
        No pior caso (árvore desbalanceada): O(n)
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
        # Se for igual, não fazemos nada (chaves duplicadas não são permitidas)
    
    def search(self, key):
        """
        Busca por uma chave na árvore.
        Complexidade: O(h), onde h é a altura da árvore.
        No pior caso (árvore desbalanceada): O(n)
        """
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
    
    def remove(self, key):
        """
        Remove um nó da árvore.
        Complexidade: O(h), onde h é a altura da árvore.
        No pior caso (árvore desbalanceada): O(n)
        """
        self.root = self._remove(self.root, key)
    
    def _remove(self, node, key):
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
            
            # Nó com dois filhos: obter o sucessor in-order (menor na subárvore direita)
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._remove(node.right, temp.key)
        
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder(self):
        """
        Percurso in-order (em-ordem).
        Complexidade: O(n), pois visita cada nó exatamente uma vez.
        """
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)
    
    def preorder(self):
        """
        Percurso pre-order (pré-ordem).
        Complexidade: O(n), pois visita cada nó exatamente uma vez.
        """
        result = []
        self._preorder(self.root, result)
        return result
    
    def _preorder(self, node, result):
        if node:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
    
    def postorder(self):
        """
        Percurso post-order (pós-ordem).
        Complexidade: O(n), pois visita cada nó exatamente uma vez.
        """
        result = []
        self._postorder(self.root, result)
        return result
    
    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)