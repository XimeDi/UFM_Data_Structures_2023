from circular_queue import CircularQueue


# Queue instance
queue = CircularQueue(5)
print(queue)

# Enqueues
queue.circular_enqueue('A')
print(queue)
queue.circular_enqueue('B')
print(queue)
queue.circular_enqueue('C')
print(queue)
queue.circular_enqueue('D')
print(queue)
queue.circular_enqueue('E')
print(queue)
queue.circular_enqueue('F') # Queue Overflow
queue.circular_enqueue('G') # Queue Overflow

#Search
print('Search, key = D', queue.circular_search('D'))
print('Search, key = H', queue.circular_search('H'))

#Peek
print(queue)
print('Peek:', queue.peek())

# Dequeues
queue.circular_search()
print(queue)
queue.circular_search()
print(queue)
queue.circular_search()
print(queue)
print('Peek:', queue.peek())
print(queue)
queue.circular_search()
print(queue)
queue.circular_search()
print(queue)

print('Search, key = J', queue.circular_search('J')) #Queue Underflow 