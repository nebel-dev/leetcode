"""
257.Binary Tree Paths
"""
# definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :param root:TreeNode
        :return:List[str]
        """
        paths = []
        def constract_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    constract_paths(root.left, path)
                    constract_paths(root.right, path)
        constract_paths(root, '')


