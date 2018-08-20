'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 '''

def count_unival(tree):
    return count_unival_length(0, tree, tree[0])

# Count unival length with length greater than 1
def count_unival_length(pos, tree):

 
if __name__ == '__main__':
    array = input("Enter binary tree array: ")
    print(count_unival(array))