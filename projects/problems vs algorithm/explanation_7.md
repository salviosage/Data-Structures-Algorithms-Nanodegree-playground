## HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.
first I have initialized a RouteTrieNode, which has value, handler & reference to next node. then I have utilized this node to implement RouteTrie.

RouteTrieNode:

Time Complexity - O(1) Space Complexity - O(1)

RouteTrie:

Time Complexity - O(n) Space Complexity - O(n) (lookup, add handler)