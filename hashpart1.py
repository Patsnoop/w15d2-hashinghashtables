# First create a class for storing key-value pairs in the linked list for chaining.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Implement hast table with chaining for collision resolution.

class HashTable:
    def __init__(self, initial_capacity = 10, load_factor=0.75):
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [None] * self.capacity

    # Implement hash function to convert a key into an index in the buckets array
    def _hash(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.capacity
        return hash_value
    
    # Implement way to resize the hash table when the load factor exceeds the threshold
    def _resize(self):
        new_capacity = self.capacity * 2
        new_buckets = [None] * new_capacity
        old_buckets = self.buckets
        self.buckets = new_buckets
        self.capacity = new_capacity
        self.size = 0

        for node in old_buckets:
            while node:
                self.insert(node.key, node.value)
                node = node.next


    # Insert a key value pair into the hash table
    def insert(self, key, value):
        if self.size / self.capacity >= self.load_factor:
            self._resize()

        index = self._hash(key)
        new_node = Node(key, value)
        current_node = self.buckets[index]

        if not current_node:
            self.buckets[index] = new_node
        else:
            while current_node:
                if current_node.key == key:
                    current_node.value = value
                    return
                if not current_node.next:
                    current_node.next = new_node
                    break
                current_node = current_node.next

        self.size +=1

    # Retrieve the value associated with a given key
    def get(self, key):
        index = self._hash(key)
        current_node = self.buckets[index]

        while current_node:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next

        return None
    

    # Delete a key-value pair from the hash table

def remove(self, key):
    index = self._hash(key)
    current_node = self.buckets[index]
    prev_node = None

    while current_node:
        if current_node.key == key:
            if prev_node:
                prev_node.next = current_node.next
            else:
                self.buckets[index] = current_node.next
            self.size -= 1
            return
        prev_node = current_node
        current_node = current_node.next



