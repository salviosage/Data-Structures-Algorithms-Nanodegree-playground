#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Your work here
import sys
global huff

def huffman_encoding(data):
    global huff
    huff = {}
    print(not data)
    if not data:
        return data, None
    for char in data:
        huff[char] = huff.get(char, 0) + 1
    tree = {}
    temp = '1'
    for num in sorted(huff.items(), key = lambda x: x[1]):
        tree[num[0]] = temp
        temp = '0' + temp

    encode = ''
    for d in data:
        encode += tree[d]
    return encode, tree

def huffman_decoding(data,tree):
    huff = {}
    for char in tree:
        huff[tree[char]] = char
    #print(huff)
    temp = ''
    decode = ''
    for d in data:
        if d == '1':
            decode += huff[temp + d]
            temp = ''
        else:
            temp += d
    return decode

if __name__ == "__main__":
    codes = {}
def testcases(a_great_sentence):
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    if not encoded_data:
        print ("The size of the encoded data is 0")
        print ("The content of the encoded data is null")
        print ("The size of the decoded data is 0")
        print ("The content of the encoded data is null")
    else:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

first_sentence = "The bird is the word"
second_sentence = "aaaaaaaaaa"
third_sentence = "" 
testcases(first_sentence)  
testcases(second_sentence) 
testcases(third_sentence)

# In[ ]:




