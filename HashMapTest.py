from HashMap import HashMap
import unittest

class HashMapTest(unittest.TestCase):
    def testHashMapInit(self):
        hm = HashMap(3)
        self.failUnless(hm)
    def testIncorrectSize(self):
        self.assertRaises(ValueError, HashMap, 0)

    def testSizeNotInt(self):
        self.assertRaises(TypeError, HashMap, "Uh-Oh")

    def testSetElement(self):

    def testFull(self):

    def testLoad(self):
