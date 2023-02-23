from queue import LinearQueue


# Queue instance
queue = LinearQueue(5)
print(queue)

# Enqueues
queue.enqueue('A')
print(queue)
queue.enqueue('B')
print(queue)
queue.enqueue('C')
print(queue)
queue.enqueue('D')
print(queue)
queue.enqueue('E')
print(queue)
queue.enqueue('F') # Queue Overflow
queue.enqueue('G') # Queue Overflow

#Search
print('Search, key = D', queue.search("D"))
print('Search, key = H', queue.search("H"))

#Peek
print(queue)
print('Peek:', queue.peek())

# Dequeues
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
print('Peek:', queue.peek())
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue() # Queue Underflow (2nd scenario)
queue.dequeue() # Queue Underflow (2nd scenario)

queue_2 = LinearQueue(5)
print(queue_2)
queue.dequeue() # Queue Underflow (1st scenario)
