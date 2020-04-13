class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"key: {self.key} - value: {self.value} - next: {self.next}"

    def __repr__(self):
        return f"key: {self.key} - value: {self.value} - next: {self.next}"
    
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0
    
    def _hash(self, key):
        return hash(key) 
    
    def _hash_mod(self, key):
        return self._hash(key) % self.capacity
        
    def insert(self, key, value):
        index = self._hash_mod(key)
        newNode = ListNode(key, value)
        print(index)
        if self.storage[index] is None:
            self.storage[index] = newNode
        else:
            currHead = self.storage[index]    
            while currHead is not None:
                currHead = currHead.next
            currHead.next = newNode
    
    def get_storage(self):
        for item in self.storage:
            print(item)

newHashTable = HashTable(8)
newHashTable.insert("apple", "red")
newHashTable.insert("pear", "green")
newHashTable.get_storage()
