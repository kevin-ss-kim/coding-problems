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
    return count_unival_length(0, tree, -1)

def count_unival_length(pos, tree, chain_pos):
    print("calling count_unival_length (%s, %s)" % (str(pos), str(chain_pos)))
    if pos >= len(tree):
        return 0
    match_parent, extra_value, new_chain_pos = 0, 0, pos
    if tree[pos] == tree[chain_pos]:
        match_parent = 1
    # Check if the pos is at least left grandchild of chain_pos
    if chain_pos >= 0 and chain_pos * 4 + 3 <= pos and tree[chain_pos] == tree[pos]:
        extra_value = 1
        new_chain_pos = chain_poss
    left_unival_count = count_unival_length(2 * pos + 1, tree, new_chain_pos)
    right_unival_count = count_unival_length(2 * pos + 2, tree, new_chain_pos)
    return left_unival_count + right_unival_count + extra_value + match_parent
    
# Define binary tree as array
# Given a node at index n, the left and right child
# are located at 2n + 1 and 2n + 2 respectively
if __name__ == '__main__':
    array = input("Enter binary tree array: ")
    print(count_unival(array))