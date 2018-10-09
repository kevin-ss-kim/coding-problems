'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''
class Trie():

    class TrieNode():
        def __init__(self):
            self.children = {}
            self.value = None

    def __init__(self):
        self.root = self.TrieNode()

    def find(self, root, key):
        node = root
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def insert(self, root, string):
        node = root
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = self.TrieNode()
                node.children[char] = newNode
                node = newNode
        node.value = string

def find_all_prefix_strings(array, s):
    trie = convert_to_trie(array)
    node = trie.find(trie.root, s)
    return find_all_prefix_strings_recursive(node)

def find_all_prefix_strings_recursive(node):
    strings = []
    if node.value != None:
        strings.append(node.value)
    for char in node.children:
        strings_children = find_all_prefix_strings_recursive(node.children[char])
        if len(strings_children) > 0:
            strings += strings_children
    return strings

# Converts array of strings to a trie
def convert_to_trie(array):
    trie = Trie()
    for string in array:
        trie.insert(trie.root, string)
    return trie

if __name__ == '__main__':
    array = input("Enter array of strings: ")
    s = input("Enter query string: ")
    print(find_all_prefix_strings(array, s))