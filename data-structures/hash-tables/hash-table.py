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
        if self.storage[index] is None:
            self.storage[index] = newNode
        else:
            currHead = self.storage[index]    
            prevNode = None
            while currHead is not None and currHead.key != key:
                prevNode = currHead
                currHead = currHead.next

            if currHead is None:
                prevNode.next = newNode
            else:
                currHead = newNode
    
    def find(self, key):
        index = self._hash_mod(key)
        currHead = self.storage[index]

        while currHead is not None and currHead.key != key:
            currHead = currHead.next
        
        if currHead is None:
            return None

        return currHead.key
    
    def remove(self, key):
        index = self._hash_mod(key)
        prevNode = None
        currHead = self.storage[index]

        while currHead is not None and currHead.key != key:
            prevNode = currHead
            currHead = currHead.next
        
        if currHead is None:
            print("Item unavailable")
        else:
            print(f"Deleted {key}")
            if prevNode is None:
                currHead = None
            else:
                prevNode.next = currHead.next


    def get_storage(self):
        for item in self.storage:
            print(item)

newHashTable = HashTable(8)
newHashTable.insert("apple", "red")
newHashTable.insert("pear", "green")
newHashTable.insert("kiwi", "green")
newHashTable.insert("mango", "orange")
newHashTable.insert("orange", "orange")
newHashTable.insert("banana", "yellow")
# print(newHashTable.find("banana"))
# print(newHashTable.find("orange"))
# print(newHashTable.find("papaya"))
newHashTable.get_storage()
newHashTable.remove("banana")
newHashTable.remove("coconut")
newHashTable.get_storage()
