'''
Stack: Last in, first out (LIFO)
    Uses:
    - Undo history
    - Call stacks
    - Bracket matching
    - Depth first search (DFS)
Queue: First in, first out (FIFO)
    Uses:
    - Task scheduling
    - Breadth first search (BFS)
    - Buffering
    - Print queues
'''

# LIFO: push to top, pop from top
class Stack:
    def __init__(self):
        self._data = []

    # Add item to the top of the stack
    def push(self, item) -> None:
        self._data.append(item)

    # Remove and return top item. Loud fail if stack is empty (IndexError)
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack.")
        return self._data.pop()

    # Return the top item without removing it.
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek at empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return  len(self._data) == 0

    def size(self) -> int:
        return  len(self._data)

    def __repr__(self):
        return f"Stack(top -> {self._data[::1]}"

# FIFO: enqueue at the back, dequeue from the front
class Queue:
    def __init__(self):
        self._data = []

    # Add item to the back of the queue
    def enqueue(self, item) -> None:
        self._data.append(item)

    # Remove & return front item
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue.")
        return self._data.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek at empty queue.")
        return self._data[0]

    def is_empty(self) -> bool:
        return  len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __repr__(self):
        return f"Queue(front -> {self._data}"

if __name__ == "__main__":
    print("--- Stack ---")
    s = Stack()
    for i in [1, 2, 3]:
        s.push(i)
    print(s)
    print("Pop:", s.pop())
    print("Peek:", s.peek())
    print(s)

    print("\n--- Queue ---")
    q = Queue()
    for i in [1, 2, 3]:
        q.enqueue(i)
    print(q)
    print("Dequeue:", q.dequeue())
    print("Peek:", q.peek())
    print(q)