class Node:
    def __init__(self, key, value):
        # Actual cache information
        self.key = key
        self.value = value

        # Doubly linked-list pointers
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # Dictionary:
        # key -> Node
        #
        # This lets us find the Node for a key in O(1) average time.
        self.cache = {}

        # Dummy nodes marking the two ends of our linked list.
        #
        # left  = LRU side
        # right = MRU side
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Initially the list is empty:
        #
        # left <-> right
        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        # Remove an EXISTING node from wherever it currently is.
        #
        # Example:
        # 1 <-> 2 <-> 3
        #
        # remove(2)
        #
        # 1 <-> 3

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    def insert(self, node):
        # Insert an EXISTING node at the MRU (right) end.
        #
        # Example:
        # 1 <-> 3
        #
        # insert(2)
        #
        # 1 <-> 3 <-> 2
        #              ↑
        #             MRU

        prev_node = self.right.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:

        # Key doesn't exist in the cache
        if key not in self.cache:
            return -1

        # Dictionary gives us the EXISTING Node directly.
        node = self.cache[key]

        # Getting the key means it was just used,
        # so it becomes the most recently used.
        self.remove(node)
        self.insert(node)

        # Return the value stored inside that Node.
        return node.value


    def put(self, key: int, value: int) -> None:

        # If key already exists,
        # remove its old Node from the linked list.
        if key in self.cache:
            self.remove(self.cache[key])

        # Create a new Node containing this key and value.
        node = Node(key, value)

        # Store the Node in the dictionary.
        #
        # key -> Node
        self.cache[key] = node

        # New/updated key is now the most recently used.
        self.insert(node)

        # If we exceeded capacity,
        # we must remove the least recently used Node.
        if len(self.cache) > self.capacity:

            # left.next is the actual LRU Node.
            lru = self.left.next

            # Remove it from the linked list.
            self.remove(lru)

            # Also remove its key from the dictionary.
            del self.cache[lru.key]