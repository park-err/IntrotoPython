from LinkedList import LinkedList
from Node import Node

class Queue:
    def __init__(self):
        self.list = LinkedList()
        
    def push(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)
        
        # Insert as list tail (end of queue)
        self.list.append(new_node)
    
    def pop(self):
        # Copy data from list's head node (queue's top node)
        popped_item = self.list.head.data
        
        # Remove list head
        self.list.remove_after(None)
        
        # Return the popped item
        return popped_item


num_queue = Queue()
num_queue.push(17)
num_queue.push(24)
num_queue.push(18)

# Output queue
print('Queue after push:', end=' ')
node = num_queue.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()

num_queue.pop()  # Pop 17

# Output final queue
print('Queue after pop:', end=' ')
node = num_queue.list.head
while node != None:
   print(node.data, end=' ')
   node = node.next
print()
