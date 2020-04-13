## HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.
first I have initialized a RouteTrieNode, which has value, handler & reference to next node. then I have utilized this node to implement RouteTrie.

## Efficiency ##

### Time efficiency ###

RouteTrieNode:

while creating a routeTrie noode basically we will have to connect new node to the parent node 

Time Complexity - `O(1)` Space Complexity - `O(1)`


RouteTrie:

here in RouteTrie we will have to loop through all subroutes included in route to make a trie of the route so suppose that we have route with (`s`) subroutes 

Time Complexity - `O(s)` Space Complexity - `O(s)`


The solution to lookup path requires that we first locate the "root" node, and navigate through its subroutes tp identify its handler 

The worst-case scenario is that the route has child node . For example, the path contavin /home/about .

In this case, we would need to visit every node in the entire Routertrie. to find handler much those subroutes. so we have route and route have subroutes(`l`)

This gives us a time efficiency of `O(l)`.

