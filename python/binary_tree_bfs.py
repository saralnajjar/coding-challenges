"""
Binary Tree Level Order Traversal.
Builds a binary tree and traverses it level by level using a queue.
Returns each level as its own list. 

"""

from collections import deque


class Node:
    def __init__(self, value: int, left: 'Node | None' = None, right: 'Node | None' = None):
        self.value = value
        self.left = left
        self.right = right


def bfs(root: Node | None) -> list[list[int]]:
    """Return a list of levels, each level being a list of node values."""
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


def run_test(description: str, actual: list, expected: list) -> bool:
    status = "PASS" if actual == expected else "FAIL"
    print(f"  {status}  {description}")
    if actual != expected:
        print(f"         expected: {expected}")
        print(f"         got:      {actual}")
    return actual == expected


def main() -> None:
    print("Binary Tree - Level Order Traversal (BFS)")
    print("=" * 45)

    tree = Node(1,
        Node(2, Node(4), Node(5)),
        Node(3, None, Node(6))
    )
    run_test("full tree", bfs(tree), [[1], [2, 3], [4, 5, 6]])

    # Single node
    run_test("single node", bfs(Node(42)), [[42]])

    # Empty tree
    run_test("empty tree", bfs(None), [])

    # Left-skewed tree: 1 -> 2 -> 3
    skewed = Node(1, Node(2, Node(3)))
    run_test("left-skewed", bfs(skewed), [[1], [2], [3]])

    # Complete binary tree
    complete = Node(1, Node(2), Node(3))
    run_test("complete 3-node tree", bfs(complete), [[1], [2, 3]])


if __name__ == "__main__":
    main()