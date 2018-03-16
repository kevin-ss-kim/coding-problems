from BinaryTreeNode import *

def find_second_largest_element(array):
    array = sorted(array)
    answer = generateBinaryTree()
    return answer

if __name__ == '__main__':
    array = input("Enter array: ")
    print(find_second_largest_element(array))