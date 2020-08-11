from linked_list import LinkedList

class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [LinkedList()] * capacity
        self.entries = 0


    def get_num_slots(self):
        # Your code here
        return self.capacity


    def get_load_factor(self):
        # Your code here
        return self.entries / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for i in key:
            hash = ((hash << 5) + hash) + ord(i)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)
        slot = self.storage[index]
        current = slot.head

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        newElement = HashTableEntry(key, value)
        slot.insert(newElement)
        self.entries += 1

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        index = self.hash_index(key)
        slot = self.storage[index]
        current = slot.head

        while current is not None:
            if current.key == key:
                slot.delete(current.value)
                self.entries -= 1
                if self.get_load_factor() < 0.2:
                    self.resize(int(self.capacity * .5))
                return
            current = current.next
        return None

    def get(self, key):
        index = self.hash_index(key)
        slot = self.storage[index]
        current = slot.head

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def resize(self, new_capacity):
        if new_capacity < MIN_CAPACITY:
            resize_capacity = MIN_CAPACITY
        else:
            resize_capacity = new_capacity

        storage_copy = self.storage
        self.storage = [LinkedList()] * resize_capacity
        self.entries = 0
        self.capacity = resize_capacity
        for each_item in storage_copy:
            current = each_item.head
            while current is not None:
                self.put(current.key, current.value)
                current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
