class Stack:
    def __init__(self):
        self.storage = []
        self.size = 0
    
    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.storage.pop()

new_stack = Stack()
new_stack.push(1)
new_stack.push(2)