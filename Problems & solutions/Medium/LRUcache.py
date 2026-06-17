# Approach:
# Combine a hashmap and a doubly linked list to support O(1) access and updates.
# The hashmap maps keys to nodes, while the doubly linked list maintains usage
# order from least recently used (LRU) to most recently used (MRU). On every
# get or put, move the accessed node to the MRU position. When capacity is
# exceeded, remove the LRU node from both the list and the hashmap.
#
# Time: O(1) per get/put operation
# Space: O(capacity)


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # Maps key to node
        self.cache = {}
        # Points to LRU
        self.left = Node(0, 0)
        # Points to MRU
        self.right = Node(0, 0)

        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
