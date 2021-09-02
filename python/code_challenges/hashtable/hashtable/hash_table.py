from hashtable.linked_list import *

class HashTable:

    def __init__(self, size = 1024):
        self.size = size
        self._buckets = [None] *self.size



    def hash(self,key:str)->int:
        value=0
        for x in key:
            value += ord(x)
        index = (value * 7) % self.size
        return index


