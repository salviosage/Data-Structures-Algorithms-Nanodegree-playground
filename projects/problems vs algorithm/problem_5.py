import collections


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

    def suffixes(self):
        """
        Find all of the node's suffixes
        :return: list
        """

        def recurse(nodes, prefix):
            suffixes = []

            for letter, node in nodes.items():
                if node.is_word:
                    suffixes.append(prefix + letter)
                if node.children:
                    suffixes += recurse(node.children, prefix + letter)

            return suffixes

        return recurse(self.children, '')


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Add a word to the trie
        :param word: string
        """
        current_node = self.root
        for char in word:
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, letters):
        """
        Retrieve the given sequence of letters in the trie, and return the terminating node
        :param letters: string
        :return: TrieNode|None
        """
        node = self.root

        for letter in letters:
            if letter not in node.children:
                return None
            node = node.children[letter]

        return node

    def exists(self, word):
        """
        Check if the trie contains a given word
        :param word: string
        :return: bool
        """

        node = self.find(word)
        return False if node is None else node.is_word

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Find
assert type(MyTrie.find('ant')) is TrieNode
assert MyTrie.find('salvi') is None

# Exists
assert not MyTrie.exists('anthony')
assert not MyTrie.exists('sal')
assert not MyTrie.exists('zzz')
assert MyTrie.exists('ant')
assert  MyTrie.exists('anthology')


# Suffixes
node = MyTrie.find('a')
assert node.suffixes() == ['nt', 'nthology', 'ntagonist', 'ntonym']

node = MyTrie.find('ant')
assert node.suffixes() == ['hology', 'agonist', 'onym']

node = MyTrie.find('anto')
assert node.suffixes() == ['nym']

node = MyTrie.find('trie')
assert node.suffixes() == []
