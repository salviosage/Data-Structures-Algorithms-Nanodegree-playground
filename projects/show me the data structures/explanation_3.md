- I have implemented huffman encoding technique here with following steps:

- Calculate the occurences of each characters in a string.
- Character with highest occurence is encoded with minimum code length ie 1
then next Character as 01 and then 001 and so on.

- Time complexity: O(n)
- Space complexity: O(distinct_characters)