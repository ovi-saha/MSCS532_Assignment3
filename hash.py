class HashNode:    #HashNode Class
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Pointer to the next node in the chain


class HashTable: #HashTable Class
    def __init__(self, size=10): #giving a default table size 10
        self.size = size  # Size of the hash table
        self.table = [None] * self.size  # Array of linked lists (chains)

    def hash(self, key):
        return hash(key) % self.size  # Hash function

    def insert(self, key, value):
        index = self.hash(key)
        new_node = HashNode(key, value)
        
        # If the chain at this index is empty, insert the new node
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            # Collision: traverse the chain and update or append the new node
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value  # Update the value if key already exists
                    return
                if current.next is None:  # Reach the end of the chain
                    break
                current = current.next
            current.next = new_node  # Append new node to the chain

    def search(self, key):
        index = self.hash(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value  # Return value if key is found
            current = current.next
        
        return None  # Key not found

    def delete(self, key):
        index = self.hash(key)
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next  # Bypass the current node
                else:
                    self.table[index] = current.next  # Update head of the chain
                return True  # Key was found and deleted
            prev = current
            current = current.next
        
        return False  # Key not found


# Example usage
hash_table = HashTable()
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)

print(hash_table.search("banana"))  # Output: 2
print(hash_table.delete("apple"))    # Output: True
print(hash_table.search("apple"))     # Output: None