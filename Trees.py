
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
    

#543 Diameter of binary tree. Basic DFS, comparing taking node with greatest diameter starting at bottom
class Diameter:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]
    

# 110. is binary tree balanced. For each node, find and return if balanced and height. 
# Condition for node being balanced is that each sub node is balanced and difference between height of subnodes is less than 2
class isBalanced:
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(node) -> [bool, int]:
            if not node:
                return [True, 0]
            
            left, right = dfs(node.left), dfs(node.right)

            balanced = (abs(left[1] - right[1]) <= 1 and left[0] and right[0])

            height = 1 + max(left[1], right[1])

            return [balanced, height]

        
        answer = dfs(root)
        
        return answer[0]
        