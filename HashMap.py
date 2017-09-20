'''
This fixed-size hash map associates string keys
with arbitrary data object references using only primitive types.
Author - Allison Tielking
'''

from math import ceil, log

class HashMap:
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("Size parameter must be of type int.")
        if size < 1:
            raise ValueError("HashMap must have a size of at least 1.")
        self.itemCount = 0
        self.hashMapSize = size
        self.buckets = int(pow(2, ceil(log(size, 2))))
        self.hashMap = [[] for item in range(self.buckets)]

    def set(self, key, value):
        '''
        This function stores the given key/value pair in the hash map. It
        returns a Boolean indicating whether the operation was successful.
        '''
        if self.itemCount == self.hashMapSize: return False #hashmap has reached capacity
        else:
            position = key.__hash__() % self.buckets
            bucket = self.hashMap[position] #gets hash index for key
            for index, (k, val) in enumerate(bucket): #searches for key in bucket list
                if k == key: #overwrites if key already in bucket
                    if val != value: bucket[index] = (key, value)
                    return True
            #key not in map yet
            self.itemCount += 1
            bucket.append((key, value))
            return True

    def get(self, key):
        '''
        This function returns the *value* associated with the given key, or
        it returns null if the key cannot be found.
        '''
        position = key.__hash__() % self.buckets
        bucket = self.hashMap[position]
        for index, (k, val) in enumerate(bucket):
            if k == key: return val #returns value of key
        return None #key was not found


    def delete(self, key):
        '''
        This function deletes the value associated with a given key. It
        returns the value if the operation is successful, or null if the
        key has no value.
        '''
        position = key.__hash__() % self.buckets
        bucket = self.hashMap[position]
        for index, (k, val) in enumerate(bucket):
            if k == key:
                bucket[index] = (k, None)
                return val
        return None

    def load(self):
        '''
        This function returns a float value that represents the current load
        factor of the hash map. We calculate this value by dividing the total
        number of items in the map by the size of the map.
        '''
        return self.itemCount / float(self.hashMapSize)

    def printHashMap(self):
        '''
        Prints all of the hash map's keys and values
        '''
        return self.hashMap
