class Array:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.size = 0
    
    def __str__(self):
        return f"{self.storage}"

    def insert(self, item):
        for i in range(len(self.storage) - 1, 0, -1):
            self.storage[i] = self.storage[i - 1]
            print(self.storage[i], self.storage[i- 1])
            print(i, i- 1)

        self.storage[0] = item
        self.size += 1

newArray = Array(8)
print(newArray)
newArray.insert(3)
newArray.insert(4)
newArray.insert(5)
newArray.insert(6)
newArray.insert(7)
newArray.insert(8)
newArray.insert(9)
newArray.insert(10)
newArray.insert(11)
print(newArray)