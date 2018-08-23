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
    return count_unival_length(0, tree, None)

# For any given node, the unival count is
# 1 if the node value is equal to left or right child
# 3 if the node value is equal to left and right child
def count_unival_length(pos, tree, parent_value):
    if pos >= len(tree):
        return 0
    match_parent, extra_value = 0, 0
    if tree[pos] == parent_value:
        match_parent = 1
    left_unival_count = count_unival_length(2 * pos + 1, tree, tree[pos])
    right_unival_count = count_unival_length(2 * pos + 2, tree, tree[pos])
    if left_unival_count and right_unival_count:
        extra_value = 1
    return left_unival_count + right_unival_count + match_parent + extra_value
    
# Define binary tree as array
# Given a node at index n, the left and right child
# are located at 2n + 1 and 2n + 2 respectively
if __name__ == '__main__':
    array = input("Enter binary tree array: ")
    print(count_unival(array))