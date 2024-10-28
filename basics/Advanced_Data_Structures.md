Advanced data structures in Python extend beyond basic types like lists, sets, and dictionaries. They are designed to optimize performance for specific use cases, enhance code organization, and enable more efficient data manipulation. Here are some of the key advanced data structures available in Python:

### 1. **Heaps**

A **heap** is a special tree-based data structure that satisfies the heap property, where the parent node is either greater than or equal to (max heap) or less than or equal to (min heap) its children. Python provides a built-in `heapq` module for implementing heaps.

#### Example of Using `heapq`

```python
import heapq

# Create a min heap
numbers = [5, 2, 9, 1, 5, 6]
heapq.heapify(numbers)  # Transform list into a heap
print(numbers)  # Output: [1, 2, 9, 5, 5, 6]

# Push a new element onto the heap
heapq.heappush(numbers, 0)
print(numbers)  # Output: [0, 1, 9, 2, 5, 6, 5]

# Pop the smallest element
smallest = heapq.heappop(numbers)
print(smallest)  # Output: 0
print(numbers)  # Output: [1, 2, 9, 5, 5, 6]
```

### 2. **Linked Lists**

While Python does not have a built-in linked list type, you can implement your own using classes. A linked list consists of nodes, where each node contains data and a reference to the next node.

#### Example of a Singly Linked List

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  # Output: 1 -> 2 -> 3 -> None
```

### 3. **Trees**

Trees are hierarchical data structures consisting of nodes connected by edges. The most common type of tree is the binary tree, where each node has at most two children.

#### Example of a Binary Tree

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_recursively(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                self._insert_recursively(node.right, value)
            else:
                node.right = TreeNode(value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

bt = BinaryTree()
bt.insert(5)
bt.insert(3)
bt.insert(7)
bt.inorder_traversal(bt.root)  # Output: 3 5 7
```

### 4. **Graphs**

Graphs consist of nodes (vertices) connected by edges. They can be directed or undirected and can contain cycles. You can represent graphs using adjacency lists or adjacency matrices.

#### Example of a Graph Using an Adjacency List

```python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.print_graph()
# Output:
# 0: [1, 2]
# 1: [2]
```

### 5. **Queues and Deques**

Python provides a built-in `queue` module and `collections.deque` for implementing queues and double-ended queues (deques). Queues follow FIFO (First-In-First-Out) order, while deques allow you to add or remove elements from both ends efficiently.

#### Example of Using `collections.deque`

```python
from collections import deque

# Creating a deque
dq = deque()

# Adding elements to the right
dq.append(1)
dq.append(2)

# Adding elements to the left
dq.appendleft(0)

# Removing elements
print(dq.pop())       # Output: 2
print(dq.popleft())   # Output: 0
print(dq)             # Output: deque([1])
```

### 6. **Priority Queues**

Priority queues are special types of queues where each element has a priority. Elements with higher priority are dequeued before elements with lower priority. You can implement priority queues using the `heapq` module.

### 7. **Custom Data Structures**

You can create custom data structures tailored to your specific needs by combining built-in types and implementing necessary methods. This flexibility allows you to design efficient structures that suit your application's requirements.

### Summary

- **Heaps**: Efficient for priority queue operations.
- **Linked Lists**: Useful for dynamic data that needs frequent insertions and deletions.
- **Trees**: Hierarchical data structure ideal for representing sorted data.
- **Graphs**: Complex relationships between nodes, useful in various applications (e.g., social networks, routing).
- **Queues and Deques**: For managing data in FIFO order and providing efficient access from both ends.
- **Priority Queues**: For managing data with associated priorities.

By leveraging these advanced data structures, you can optimize your code's performance and maintainability, allowing for efficient data management and manipulation.
