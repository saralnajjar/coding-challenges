"""
Least recently used cache build using a double kinked list and a hash map.
Both get and put run in O(1) time.
- Double linked list tracks access order: most recent at the tail, least recent at the head.
- Hash map gives O(1) node lookup by key.
"""

class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: 'Node | None' = None
        self.next: 'Node | None' = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_tail(self, node: Node) -> None:
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_at_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._insert_at_tail(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

def run_test(description: str, actual, expected) -> None:
    status = "PASS" if actual == expected else "FAIL"
    print(f"  {status}  {description}")
    if actual != expected:
        print(f"         expected: {expected}")
        print(f"         got:      {actual}")

def main() -> None:
    print("LRU Cache")
    print("=" * 45)

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    run_test("get(1) = 1", cache.get(1), 1)

    cache.put(3, 3)
    run_test("get(2) = -1 after eviction", cache.get(2), -1)
    run_test("get(3) = 3", cache.get(3), 3)

    cache.put(4, 4)
    run_test("get(1) = -1 after eviction", cache.get(1), -1)
    run_test("get(3) = 3", cache.get(3), 3)
    run_test("get(4) = 4", cache.get(4), 4)

    cache2 = LRUCache(2)
    cache2.put(1, 10)
    cache2.put(1, 20)
    run_test("update key 1 to 20", cache2.get(1), 20)

    cache3 = LRUCache(1)
    cache3.put(1, 1)
    cache3.put(2, 2)
    run_test("capacity 1: get(1) = -1", cache3.get(1), -1)
    run_test("capacity 1: get(2) = 2", cache3.get(2), 2)

    cache4 = LRUCache(3)
    run_test("get on empty cache = -1", cache4.get(99), -1)


if __name__ == "__main__":
    main()