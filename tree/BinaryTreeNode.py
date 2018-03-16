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

def generateBST(sortedArray):
    length = len(sortedArray)
    if length > 0:
        pivot = len(sortedArray) / 2
        node = BinaryTreeNode(pivot)
        leftNode = generateBST(sorted[0:pivot])
    else:
        return None