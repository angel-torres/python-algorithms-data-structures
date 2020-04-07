from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        self.storage.add_to_head(item)

        if self.storage.length == self.capacity + 1:
            self.storage.remove_from_tail()

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        while self.storage.head.next is not None:
            list_buffer_contents.append(self.storage.head.value)
            self.storage.head = self.storage.head.next
        
        list_buffer_contents.append(self.storage.head.value)

        return list_buffer_contents

newRingBuffer = RingBuffer(3)
newRingBuffer.append(1)
newRingBuffer.append(2)
newRingBuffer.append(3)
newRingBuffer.append(4)
newRingBuffer.append(5)
newRingBuffer.append(6)
newRingBuffer.append(7)
print(newRingBuffer.storage)
print(newRingBuffer.get())






# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass