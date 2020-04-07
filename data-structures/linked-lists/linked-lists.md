# Linked Lists

A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer. Python does not have linked lists in its standard library. We must create this data structure using a few classes- a node class, and a linked-list class.

**Concepts to Master**
* How to create a linked list
    1. Create a ListNode Class
    2. Create a LinkedList Class
        - This class can either be doubly linked or singly linked
        - Within this class you want to define basic methods. `insert(), delete(), reverse(), find()`
* How to traverse a linked list
    - One of the best ways I've found to traverse it is to do a while loop until the head != None
    - At the end of each while loop you need to move the head along so that each time you go to the next node `self.head = self.head.next`
* How to add elements
    1. To simplify things you can just add to head
    2. Create a node with the new value that you are inserting `new_node = ListNode(value)`
    3. Then set the next value of the node to the current head `new_node.next = self.head`
    4. Lastly make the new node the current head `new_node = self.head`
* How to remove elements
    1. Create a reference to the previous_node and to original head. You can initialize it to `None`
    2. Create a while loop to go through each node until your current head's value == the value you're trying to find
        - each time you go to your next node you must not only update the head but also the previous_node
    3. Once you found the value you're trying to find set the previous' node's next to the current head's next `previous_node.next = self.head.next`
        - this will make it so that the current value you found will no longer in the list
    4. You should set the original_head reference you created back to self.head `original_head = self.head`
* How to search elements
    - Same thing as to remove except you only need the reference the original_head. Loop over list until you find value.
* Learn to do all these with a doubly-linke-list
* Learn about it's time/space complexity 
    REMOVE : O(1) if removing from head else O(n) 
    INSERT : O(1)
    FIND   : O(n)
* When would you want to use it?
    1. you need constant-time insertions/deletions from the list (such as in real-time computing where time predictability is absolutely critical)
    2. you don't know how many items will be in the list. With arrays, you may need to re-declare and copy memory if the array grows too big
    3. you don't need random access to any elements
    4. you want to be able to insert items in the middle of the list (such as a priority queue)
* Solve 2-5 algorithm applications of this data-structure