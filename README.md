# w15d2-hashinghashtables

"""
Explanation for hastpart1.py:
The Node Class represents and individual element in the chain of a linked list stored in each bucket.
The HashTable Class implements the has table with
    _hash method to compute the hash index
    _resize method to resize the table and rehash elements when the load factor exceeds the threshold
    'insert', 'get', and 'remove' method to manage key-value pairs

Load Factor and Resizing entures that the table maintains efficient performance by resizing when necessary. The default load factor is set to 0.75.

"""