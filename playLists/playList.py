import random

class Canciones:

    def __init__(self, cod, nombre, artista, album):
        self.cod = cod
        self.nombre = nombre
        self.artista = artista
        self.album= album


class DNode:
    '''
    Node object.

    Args:
        data: value to store in node

    Attributes:
        data: value stored in node
        next (Node): pointer to next node in list
    '''
    
    def __init__( self, data):
        self.prev = None
        self.data = data
        self.next = None


    #def __repr__(self):
    #   return '| Data: {} |'.format(self.data)
    

    
class DLinkedList:

    def __init__(self):
        self.start = None
        self.end = None


    def show_details(self, index):
        current_node = self.start
        count = 0
        while current_node:
            if count == index:
                print("Id:", current_node.data.cod)
                print("Nombre:", current_node.data.nombre)
                print("Artista:", current_node.data.artista)
                print("Album:", current_node.data.album)
                print("----")
                return
            count += 1
            current_node = current_node.next
        return None



    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next

    
    def traverse(self):
        '''
        Navigates every node in the list.

        Args:
            None

        Returns:
            None
        '''
        
        current_node = self.start

        while current_node is not None:
            yield current_node
            current_node = current_node.next


    def traverse_iter(self):
        '''
        Iterates trough the list using the __iter__ method.

        Args:
            None

        Returns:
            None
        '''

        for current_node in self:
            yield current_node
            

    def insert(self, value):

        new_node = DNode(value)
        new_node.next = None
        if self.start is None:
            new_node.prev = None
            self.start = new_node
            return
        last = self.start
        while (last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return


        '''

        new_node = DNode(value)
        
        if self.start is None:
            self.start = new_node
        else:
            new_node.next = self.start
            self.start.prev = new_node

        self.start = new_node
        if self.end is None:
            self.end = new_node

        print(self.start)'''


    def print_list(self):
        self.current_node = self.start
        i = 0
        while self.current_node:
            self.show_details(i)
            current_node = current_node.next
            i = i+1
        


    def play(self):
        ubic = self.start
        print(ubic)


    def search_by_name(self, nombre) -> str:

        current_node = self.start
        i = 0

        for current_node in self:

            if current_node.nombre == nombre:
                self.show_details(current_node)
                return
            else:
                i = i+1
                current_node = current_node

        if current_node.data != nombre:
            return -1
        

    def search_by_artist(self, artista) -> str:

        current_node = self.start
        i = 0

        for current_node in self:

            if current_node.artista == artista:
                self.show_details(current_node)
                return
            else:
                i = i+1
                current_node = current_node

        if current_node.data != artista:
            return -1
        

    def playList_len(self):
        current_node = self.start
        i = 0

        while current_node is not None:
            i = i+1

        return i
    

    def search_by_id(self, key) -> str:

        current_node = self.start
        i = 0

        for current_node in self:

            if current_node.cod == key:
                self.show_details(current_node)
                return
            else:
                i = i+1
                current_node = current_node

        if current_node.data != key:
            return -1


    def play_shuffle(self):
        i = 0

        while i < 11:
            random.randrange(1, 11)
            self.search_by_id(i)


    def previous(self):
        temp = self.current_node
        self.current_node = self.prev
        self.prev = temp

        self.show_details(self.current_node)

    def next(self):
        temp = self.current_node
        self.current_node = self.current_node.next
        self.prev = temp


   