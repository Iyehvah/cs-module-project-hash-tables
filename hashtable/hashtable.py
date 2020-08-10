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
        # Your code here
        # index = self.hash_index(key)
        # hash = HashTableEntry(key, value)
        # node = self.storage[index]

        # if node is not None:
        #     self.storage[index] = hash
        #     self.storage[index].next = node
        # else:
        #     self.storage[index] = hash
        #     self.entries += 1

        ## handle colisions
        #get index
        i = hash_index(key)
        #find start of linked list using index
        #insert into linked list a new HashTableEntry
        #search through list
        #if key already exists in linked list replace that value
            #else add new HashTableEntry to head of list
        



    def delete(self, key):
        # # Your code here
        # index = self.hash_index(key)
        # node = self.storage[index]
        # prev = None

        # if node.key == key:
        #     self.storage[index] = node.next
        #     return
        # while node != None:
        #     if node.key == key:
        #         prev.next = node.next
        #         self.storage[index].next = None
        #         return
            
        #     prev = node
        #     node = node.next
        # self.elements -= 1
        # return

        i = hash_index(key)
        #search through linked list for key
        #delete that node and rearrange pointers
        #return value of deleted node (or None)

    def get(self, key):
        # # Your code here
        # i = self.hash_index(key)
        # node = self.storage[i] 
        # print(node)

        # while node is not None:
        #     if node.key == key:
        #         return node.value
        #     else:
        #         node = node.next


        #retrieve index
        i = hash_index(key)
        # get the linked list at the computed index
        # search through linked list for the key
        # compare keys till you find right one
        # if it exists return value
            # else return None

    def resize(self, new_capacity):
        # Your code here
        # Make a new array that is DOUBLE the current size
        # Go through each linked list in the array
            # Go through each item and re-hash it
            # Insert the items into their new locations
        # Time complexity?

    def shrint():
        # Same as resize, but reduce but HALF



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
