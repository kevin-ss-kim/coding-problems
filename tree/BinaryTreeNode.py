class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def generateBST(array, start, end):
    if start > end:
        return None
    mid = (start + end) / 2
    node = BinaryTreeNode(array[mid])
    node.left = generateBST(array, start, mid - 1)
    node.right = generateBST(array, mid + 1, end)
    return node