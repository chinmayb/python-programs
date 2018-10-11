
* Python dictionaries are implemented as hash tables.

* Hash tables must allow for hash collisions i.e. even if two distinct keys have the same hash value, the table's implementation must have a strategy to insert and retrieve the key and value pairs unambiguously.

* Each entry in the table actually a combination of the three values: < hash, key, value >

* Python hash table is just a contiguous block of memory

* When a new dict is initialized it starts with 8 slots.

* Initial slot, i, that is checked depends on the hash of the key. 
    hash(key)

# Logical model of Python Hash table
-+------------------------+
0| <hash|key|value>  |
-+------------------------+
1|                            
-+------------------------+


* CPython uses random probing. In random probing, the next slot is picked in a pseudo random order.

