#Задание 1
class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None      

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

#Задание 2
class LinkedList:
    def __init__(self):
        self.head = None  

#Задание 3
def add_to_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    
#Задание 4
def add_to_end(self, data):
    new_node = Node(data)
    
    if self.head is None:
        self.head = new_node
        return
    
    current = self.head
    while current.next:
        current = current.next
    
    current.next = new_node

#Задание 5
def print_list(self):
    current = self.head
    
    while current:
        print(current.data, end=' ')
        current = current.next
    print()
#Задание 6
def search(self, value):
    current = self.head
    
    while current:
        if current.data == value:
            return True
        current = current.next
    
    return False    
#Задание 7
def remove_first(self):
    if self.head is None:
        return  
    
    self.head = self.head.next

#Задание 8
def count(self):
    current = self.head
    count = 0
    
    while current:
        count += 1
        current = current.next
    
    return count

#Задание 9
ll = LinkedList()

print("Введите 5 чисел:")

for _ in range(5):
    num = int(input())
    ll.add_to_end(num)

print("Ваш список:")
ll.print_list()

#Задание 10
def reverse(self):
    prev = None
    current = self.head
    
    while current:
        next_node = current.next  
        current.next = prev       
        
        prev = current
        current = next_node
    
    self.head = prev