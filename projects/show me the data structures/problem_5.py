#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Your work here

import hashlib
import datetime
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)

    def calc_hash(self, data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

# Method 0
class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp = self.last
            self.last = Block(timestamp, data, temp)
            self.last.previous_hash = temp

def get_utc_time():
      utc = datetime.datetime.utcnow()
      return utc.strftime("%d/%m/%Y %H:%M:%S")

# Method 1
block_zero = Block(get_utc_time(), "First Information", 0)
block_one = Block(get_utc_time(), "Second Information", block_zero)
block_two = Block(get_utc_time(), "third more Information", block_one)

print(block_zero.hash) # hash fuction
print(block_one.data) # second info
print(block_two.timestamp) #timestamp
print(block_one.previous_hash.data) #first onformation

temp = LinkedList()
temp.append(get_utc_time(), "Some Information")
temp.append(get_utc_time(), "Another Information")
print(temp.last.data)
print(temp.last.previous_hash.data)


# In[ ]:




