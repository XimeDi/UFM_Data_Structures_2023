'''
Binary Search Tree

Module imlplements a binary search tree and include the classes:
Search
Traverse
Find Minimum
Find Maximum
Insert
Delete

'''

class Node:

    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None


    def __repr__(self):
        return '({})'.format(self.data)
    

class BinarySearchTree:

    def __init__(self):
        self.root = None


    def insert(self, value: int):

        if self.root is None:
            self.root = Node(value)

        else:
            self._insert(value, self.root)
            
        
    def _insert(self, value: int, subtree: Node):

        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else:
                self._insert(value, subtree.left_child)
        
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                self._insert(value, subtree.right_child)

        else:
            print('Value already exists in tree...')

    
    def traverse(self, subtree: Node):
        
        print(subtree)
        
        if subtree.left_child is not None:
            self.traverse(subtree.left_child)

        if subtree.right_child is not None:
            self.traverse(subtree.right_child)


    def search(self, key: int) -> bool:

        if self.root is None:
            return False
        
        else:
            return self._search(key, self.root)


    def _search(self, key: int, subtree: Node) -> bool:

        if key == subtree.data:
            return True
        
        elif (key < subtree.data) and (subtree.left_child is not None):
            return self._search(key, subtree.left_child)
        
        elif (key > subtree.data) and (subtree.right_child is not None):
            return self._search(key, subtree.right_child)

        else:
            return False
        

    def find_min(self, subtree: Node) -> int:

        while subtree.left_child is not None:
            subtree = subtree.left_child

        return subtree


    def find_max(self, subtree: Node) -> int:

        while subtree.right_child is not None:
            subtree = subtree.right_child

        return subtree
    

    def delete_node(self, key: int, subtree: Node):

        if self.root is None:
            print("Tree is already empty")
            return None
        
        else: 
            self.root = self._delete_node(key, subtree)


    def _delete_node(self, key: int, subtree: Node) -> Node: 

        if key < subtree.data:
            subtree.left_child = self._delete_node(key, subtree.left_child)

        elif key > subtree.data:
            subtree.right_child = self._delete_node(key, subtree.right_child)

        else:
            if subtree.left_child is None:
                temp = subtree.right_child
                subtree = None
                return temp

            elif subtree.right_child is None:
                temp = subtree.left_child
                subtree = None
                return temp

            temp = self.find_min(subtree.right_child)
            subtree.data = temp.data
            subtree.right_child = self._delete_node(temp.data, subtree.right_child)

        return subtree

    

