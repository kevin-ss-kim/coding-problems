'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

def binaryTreePaths(root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if root is None: return []
    result = []
    binaryTreePathsHelper(root, '', result)
    return result
    
def binaryTreePathsHelper(root, pathSoFar, result):
    if root.left is None and root.right is None:
        result.append(pathSoFar + str(root.val))
    if root.left:
        binaryTreePathsHelper(root.left, pathSoFar + str(root.val) + "->", result)
    if root.right:
        binaryTreePathsHelper(root.right, pathSoFar + str(root.val) + "->", result)