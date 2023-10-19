
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class InvertTree:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        tmp = root.right
        root.right = root.left
        root.left = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

# 104 max depth of binary tree. Very easy
class MaxDepth:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))