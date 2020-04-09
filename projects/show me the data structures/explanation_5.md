## Blockchain ##
A linked list is used for this problem since is easier to keep track of previous item on the blockchain, retrieval for the last block is O(1) and the first one O(n).

Hash Function: the hash function is calculated ciphering the data with sha256 using utf-8 encode, then with the encoded data as hex string we add another encode that is the timestamp ciphering the data twice.

Space complexity: O(n) - total space occupied by the blockchain Time complexity: O(1) - for appending a block