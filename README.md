# Running the Code
Run HashMap: python HashMap.py <br>
Run HashMapTest: python HashMapTest.py <br>

# kpcb_hash_map
Problem:
Using only primitive types, implement a fixed-size hash map that associates string keys with arbitrary data object references (you don't need to copy the object). Your data structure should be optimized for algorithmic runtime and memory usage. You should not import any external libraries, and may not use primitive hash map or dictionary types in languages like Python or Ruby.

The solution should be delivered in one class (or your language's equivalent) that provides the following functions:

constructor(size): return an instance of the class with pre-allocated space for the given number of objects. <br>
boolean set(key, value): stores the given key/value pair in the hash map. Returns a boolean value indicating success / failure of the operation. <br>
get(key): return the value associated with the given key, or null if no value is set. <br>
delete(key): delete the value associated with the given key, returning the value on success or null if the key has no value. <br>
float load(): return a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure. Since the size of the dat structure is fixed, this should never be greater than 1. <br>
If your language provides a built-in hashing function for strings (ex. `hashCode` in Java or `__hash__` in Python) you are welcome to use that. If not, you are welcome to do something naive, or use something you find online with proper attribution.

Instructions:
Please provide the source, tests, runnable command-line function and all the resources required to compile (if necessary) and run the following program. You are free to use any coding language that compiles/runs on *nix operating systems and requires no licensed software.
