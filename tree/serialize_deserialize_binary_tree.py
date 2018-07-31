class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.serializeTree(root, '[')
    
    def serializeTree(self, root, s):
        if root is None:
            return s
        queue = [root]
        while len(queue) != 0:
            element = queue.pop(0)
            s += str(element.val) + ','
            if element.left != None:
                queue.append(element.left)
            elif element.val != 'null':
                queue.append(TreeNode('null'))
            if element.right != None:
                queue.append(element.right)
            elif element.val != 'null':
                queue.append(TreeNode('null'))
        s = s[:-1] + ']'
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:]
        data = data[:-1]
        array = data.split(',')
        print(array)
        root = TreeNode(array[0])
        self.deserializeArray(root, array, 0)
        return root
    
    def deserializeArray(self, root, array, index):
        if len(array) > index:
            if array[index + 1] != 'null':
                root.left = TreeNode(array[index + 1])
                self.deserializeArray(root.left, array, index + 1)
            if array[index + 2] != 'null':
                root.right = TreeNode(array[index + 2])
                self.deserializeArray(root.right, array, index + 2)