# You can create a linked list by creating a node and a linked-list class

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f'value - {self.value}, next - {self.next}'

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        return f'head - {self.head}, size - {self.size}'

    def insert(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def removeHead(self):
        if self.head == None:
            return None
        else:
            oldHead = self.head
            self.head = self.head.next 
            self.size -= 1
            return oldHead

newLinkedList = SinglyLinkedList()
print(newLinkedList)
newLinkedList.insert(4)
newLinkedList.insert(5)
newLinkedList.insert(6)
print(newLinkedList)
newLinkedList.removeHead()
print(newLinkedList)