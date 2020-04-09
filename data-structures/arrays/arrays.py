class Array:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.size = 0
    
    def __str__(self):
        return f"{self.storage} - Size: {self.size}"

    def insert(self, item):
        if self.size == self.capacity:
            print("Array is full!")
            return

        for i in range(len(self.storage) - 1, 0, -1):
            self.storage[i] = self.storage[i - 1]

        self.storage[0] = item
        self.size += 1
    
    def append(self, item):
        if self.size == self.capacity:
            self.resize()

        self.storage[self.size] = item
        self.size += 1
    
    def pop(self):
        last_item = self.storage[self.size - 1]
        self.storage[self.size - 1] = None
        self.size -= 1
        return last_item
    
    def remove(self, item):
        for i in range(self.size):
            if self.storage[i] == item:
                for i in range(i, self.size - 1, 1):
                    self.storage[i] = self.storage[i + 1]
                self.storage[self.size - 1] = None
                self.size -= 1
    
    def resize(self):
        self.capacity = self.capacity * 2
        new_storage = [None] * self.capacity
        for i in range(self.size):
            new_storage[i] = self.storage[i]

        self.storage = new_storage

newArray = Array(8)
print(newArray)
newArray.insert(3)
newArray.insert(4)
newArray.insert(5)
newArray.insert(6)
newArray.insert(7)
newArray.insert(8)
newArray.append(2)
newArray.append(1)
print(newArray)
newArray.append(9)
# print(newArray.pop())
# print(newArray.pop())
# print(newArray.pop())
# newArray.append(9)
# newArray.insert(10)
# newArray.insert(11)
print(newArray)