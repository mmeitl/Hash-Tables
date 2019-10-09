class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        # pass
        # here we find the index of the node which by using '_hash_mod' we create an integer of the key which will be the index on the list where we want to insert it
        index = self._hash_mod(key)

        # then we retrieve any preexisting node location before inserting it which should be None or occupied
        node = self.storage[index]

        # then we create a node pair using "LinkedPair" using the key and value
        pair = LinkedPair(key, value)

        # so now we have to insert the node or 'pair' as a linked list
        # we use a while loop to make sure it isn't occupied or the key of the said node doesn't exists
        while node is not None and self.storage[index].key is not key:
            # so while 'node' is not None which it should be
            # and while the found 'index' value pair key isn't the same which it shouldn't be but if a key is found  then we want to replace the value of the incomming node with the value of the node taking up it's place
            want_to_insert = node
            # so we replace the node completley here
            node = want_to_insert.next

        # now if the node is not none which it should be meaning it passes the while loop but it's currenlty being occupied by another node
        # we replace it with the inserting current's node value with the one we want to insert
        if node is not None:
            node.value = value
        else:
            # if everything passes meaning there is not matching key in the list and the current location of the node IS empty then we insert it
            # we make the preexisting node as the inserting node's next
            pair.next = self.storage[index]
            # then we replace the preexisting node with the new node
            self.storage[index] = pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        # pass
        # here we find the same information as the insert function

        # find the location of the node if it exist using the key
        index = self._hash_mod(key)

        # then we find the node using said index if it exists
        node = self.storage[index]

        # then we create a variable 'next_node' and make it none which is a 'floating' node
        next_node = None

        # while node is not None meaning it has been found and the node's key is not the same key we used to find it
        while node is not None and node.key != key:
            # we replace the None from next_node with the found node
            next_node = node
            # since the key we want doesn't match the node we found we have to delete it anyways since that can't be the case and replace it with the node
            node = next_node.next
        # if the node has been found then it skips this if statment

        # if it doesn't exist the easy easy print 'doesn't exist'
        if node is None:
            print("doesn't exist!")

        # if next_node is NONE meaning it hasn't been found again another backup
        else:
            if next_node is None:
                # we make it's current node it's next
                self.storage[index] = node.next
            else:
                # if the node exists then we just make the node equal to it's next thus 'deleteing' it
                next_node.next = node.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        # pass
        # this is pretty easy as all we're doing is getting the node from the linked list

        # so we find the node here we start with it's index
        index = self._hash_mod(key)
        # then we find the node
        node = self.storage[index]
        # if the node is not none meaning it exists
        while node is not None:
            # BUUUUUT we have to make sure the key matches the key of the retrieved peraminter
            if node.key == key:
                # if it doesn't then return it
                return node.value
                # if not then we just continue on the list
                # if it doesn't exist then we get nothing don't feel like returning anything so we just leave and the text passes so w/e lol
            node = node.next
  
    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        # pass
        # here we have to resize the capacity in case we recieve a value that exceeds what we have
        # so we do it sort of dynamicly in which we save the old storage and make a new capacity by multiplying it by 2
        old_storage = self.storage
        self.capacity *= 2
        # then reassign a new storage with the now new capacity pretty much "restarting" a new array
        self.storage = [None] * self.capacity
        # then we have to make a 'null' node in which to insert into our new storage
        # this is VERY time consuming since it takes the old storage, makes a new one, doubles the capcacity, then REINSERTS the old capacity into the new one making this o(log)n since it's depenendent on the size of the old capacity
        pair = None
        # so we use a forloop to loop through the new capcity 
        for i in old_storage:
            # with every node we have a key value pair so we make the pair equal to the old storage key value pair which is an object so
            pair = i
            # while we are inside each node we run another loop in this case a while loop to run until each key and each value is inserted thus making the node or in this case 'pair' no longer 'None'
            while pair is not None:
                # and while it is "is not None" we insert the pair's key and value into the new new storage which is "this.storage" so we use "insert"
                self.insert(pair.key, pair.value)
                # and we continue down the line of key value pairs going back and fourth through the for loop with the whole object then the while loop through the object itself.
                # again this isn't the best option and it is very costly in terms of memory and time so for large scale operation this isn't ideal at ALL
                pair = pair.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")