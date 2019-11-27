# try out the Python queue functions
# list are inefficient for queues b/c removing front element requires you to shift all the elements
# use 'deque' object in 'collections' module
from collections import deque

# TODO: create a new empty deque object that will function as a queue
queue = deque()

# TODO: add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)


# TODO: print the queue contents
print(queue)

# TODO: pop an item off the front of the queue
x = queue.popleft() # takes item in front of queue
print(x)
print(queue)