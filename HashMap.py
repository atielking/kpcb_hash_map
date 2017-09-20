'''
This fixed-size hash map associates string keys
with arbitrary data object references using only primitive types.
Author - Allison Tielking
'''

class HashMap:
    def __init__(self, size):
        self.itemCount = 0
        self.hashMapSize = size
        self.hashMap = [(None, None)] * self.hashMapSize
    def set(self, key, value):
        '''
        This function stores the given key/value pair in the hash map. It
        returns a Boolean indicating whether the operation was successful.
        '''

    def get(self, key):
        '''
        This function returns the value associated with the given key, or
        it returns null if the key cannot be found.
        '''

    def delete(self, key):
        '''
        This function deletes the value associated with a given key. It
        returns the value if the operation is successful, or null if the
        key has no value.
        '''

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
