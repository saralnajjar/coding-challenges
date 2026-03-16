'''
Each node holds a value and a pointer to the next node.
There's no fixed size.
'''

# A single node in the list, holds data and a link to th enext node
class Node:
    # Points to the next node, or non if this is the tail
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # List starts empty 
        self.head = None 
    
    '''
    Adds new node to the end of the list.
    If list is empty, node becoms head
    If not, walk to the end and attach it
    '''
    def append(self, data) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    '''
    Add a new node to the front O(1), no traversal needed
    '''
    def prepend(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    '''
    Remove the first node with this value.
    Returns True if found and deleted, False if not found.
    Special case: the dead is the node to delete.
        Otherwise find the node jyst before the one we want to delete. 
        Skip over the target node.
    '''
    def delete(self, data) -> bool:
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        return False

    '''
    Return True if a node with this value exists.
    '''
    def search(self, data) -> bool:
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    '''
    Reverse the list in place.
    Uses three pointers: prev, current, next. 
        Save the next node before we overwrite it.
        Flip the pointer backwards.
        Move prev forward.
        Move current forward.
        Prev will now be the new head 
    '''
    def reverse(self) -> None:
        prev = None
        current = self.head

        while current: 
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    '''
    For printing and testing, convert to plain list
    '''
    def to_list(self) -> list: 
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result 

if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.append(val)

    print("Original:  ", ll.to_list())

    ll.prepend(0)
    print("Prepend 0: ", ll.to_list())

    ll.delete(3)
    print("Delete 3:  ", ll.to_list())

    ll.reverse()
    print("Reversed:  ", ll.to_list())

    print("Search 4:  ", ll.search(4))
    print("Search 9:  ", ll.search(9))