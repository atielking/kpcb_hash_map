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

    def get(self, key):

    def delete(self, key):

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
