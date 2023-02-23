class CircularQueue:
    '''
    Queue object, array-based implementation. 
    Circular queue implementation.

    Args:
        size (int): size of underlying array

    Attributes:
        elements (List): array of elements
        front (int): pointer at front
        rear (int): pointer at rear
        max (int): maximum amount of elements in queue
    '''

    def __init__(self, size: int) -> None:
        self.elements = [None] * size
        self.front = -1
        self.rear = -1
        self.max = size


    def __repr__(self) -> None:
        return 'Current queue: {} | Front: {} | Rear: {}'.format(self.elements, self.front, self.rear)


    def circular_enqueue(self, value: str) -> None:
        if self.front == 0 and self.rear == self.max -1:
            print("Queue Overflow...")
            return None

        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = self.rear + 1

        if self.front != -1 and self.front == self.rear + 1:
            print("Queue Overflow...")
            return None

        self.elements[self.rear] = value

    
    def circular_dequeue(self) -> str:
        if self.front == -1:
            print("Queue Underflow...")
            return None

        value = self.elements[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            if self.front == self.max - 1:
                self.front = 0
            else:
                self.front = self.front + 1

        return value


    def circular_search(self, key: str) -> str:
        for i in range(0, self.rear + 1):
            if self.elements[i] == key:
                return i

        for j in range(self.front, self.max):
            if self.elements[i] == key:
                return i

        return -1

    def peek(self) -> str:

            if self.front == self.rear:
                return 'Queue is empty'
            
            value = self.elements[self.front]
            return value
 


