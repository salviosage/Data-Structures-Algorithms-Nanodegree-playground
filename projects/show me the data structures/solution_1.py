#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Your work here
from collections import deque

class LRU_Cache(object):
    
    def __init__(self, capacity):
        # Initialize class variables
        self.cache_capacity = capacity
        self.cache_value = {}
        self.cache_order = deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if non existant.
        if key is None:
            return -1

        return self.cache_value.get(key, -1)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if len(self.cache_order) >= self.cache_capacity:
            del self.cache_value[self.cache_order.popleft()]
        self.cache_order.append(key)
        self.cache_value[key] = value
        

    
            

    

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# In[ ]:




