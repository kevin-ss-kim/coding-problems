from BinaryTreeNode import *

def find_largest_element(root_node):
    current_node = root_node
    while current_node:
        if not current_node.right:
            return current_node.value
        current_node = current_node.right

def find_second_largest_element(root_node):
    if (root_node is None or (root_node.left is None and root_node.right is None)):
        raise Exception('Tree must have at least 2 elements')
    current_node = root_node
    while current_node:
        if current_node.left and not current_node.right:
            return find_largest_element(current_node.left)
        if (current_node.right and not current_node.right.right and not current_node.right.left):
            return current_node.value
        current_node = current_node.right

if __name__ == '__main__':
    array = input("Enter array: ")
    root_node = generateBST(array, 0, len(array) - 1)
    print(find_second_largest_element(root_node))