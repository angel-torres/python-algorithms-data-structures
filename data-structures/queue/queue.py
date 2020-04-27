class Queue:
    def __init__(self):
        self.storage = []
    
    def queue(self, value):
        self.storage.append(value)

    def dequeue(self):
        return self.storage.pop(0)


new_queu = Queue()
new_queu.queue(1)
new_queu.queue(2)
new_queu.queue(3)
print(new_queu.storage)
print(new_queu.dequeue())
print(new_queu.dequeue())
print(new_queu.storage)