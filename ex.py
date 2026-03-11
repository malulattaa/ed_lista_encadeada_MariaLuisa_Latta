

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def insert_end(self, value):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(value)
            
        else:
            self.head = Node(value)
        self.size = self.size + 1
        
    def __len__(self):
        return self.size
    
    def search(self, value):
        pointer = self.head
        i = 0
        while (pointer):
            if pointer.data == value:
                return i
            pointer = pointer.next
            i = i + 1
        return None
    # ou raise ValueError ("O elemento não está na lista")

lista = LinkedList()
lista.insert_end(7)
len(lista)