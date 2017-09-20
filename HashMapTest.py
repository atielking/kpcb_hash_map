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

    def testSetNewElement(self):
        hm = HashMap(10)
        self.assertTrue(hm.set("keyTest", "valTest"))

    def testSetOverwriteElement(self):
        hm = HashMap(10)
        h.set("keyTest1," "valTest1")
        self.assertTrue(h.set("keyTest1", "valTest3"))

    def testSetFull(self):
        hm = HashMap(2)
        h.set("keyTest1," "valTest1")
        h.set("keyTest2", "valTest2")
        self.assertFalse(h.set("keyTest3", "valTest3"))

    def testGetElementInMap(self):
        hm = HashMap(10)
        hm.set("keyTest1", "valTest1")
        self.assertIsNotNone(hm.get("keyTest1"))

    def testGetElementNotInMap(self):
        hm = HashMap(10)
        self.assertIsNone(hm.get("keyTest1"))

    def testKeyHasValue(self):
        hm = HashMap(10)
        hm.set("keyTest1", "valTest1")
        self.assertIs(hm.get("keyTest1", "valTest1"))

    def testValueOverwritten(self):
        hm = HashMap(10)
        hm.set("keyTest1", "valTest1")
        hm.set("keyTest1", "valTest2")
        self.assertIs(hm.get("keyTest1", "valTest2"))

    def testValueDeletedNotNull(self):
        hm = HashMap(10)
        hm.set("keyTest1", "valTest1")
        hm.delete("keyTest1")
        self.assertIsNone(hm.get("keyTest1"))

    def testDeleteReturnVal(self):
        hm = HashMap(10)
        hm.set("keyTest1", "valTest1")
        self.assertIs(hm.delete("keyTest1"), "valTest1")

    def testValueReturnNull(self):
        hm = HashMap(10)
        self.assertIsNone(hm.delete("keyTest1"))

    def testLoad(self):
        hm = HashMap(10)
        hm.set("keyTest1", "valTest1")
        self.assertEqual(hm.load(), 0.1)
