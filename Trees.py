import collections


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
        

# 100 Find if two trees are same. DFS. Checks if each value is same and if both left branches and both right branches are same
class isSame:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False
        elif self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False
        

#checks is one tree is subtree of another. Uses same tree checker as helper function        
class isSubTree:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        elif self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def isSameTree(self, l, r):
        if not l and not r:
            return True
        elif not l or not r or l.val != r.val:
            return False
        else:
            return self.isSameTree(l.left, r.left) and self.isSameTree(l.right, r.right)
        

#235. Lowest common ancestor of binary search tree. Was banging my head against it until I realized it was
#binary SEARCH tree. Made things real easy.
class LowestCommonAncestor:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == root or q == root:
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        

#102 Binary Tree Level Order Traversal. First BFS problem. Very easy
class LevelOrder:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        answer = []

        q = collections.deque()
        q.append(root)

        while q:
            level = []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                answer.append(level)
        
        return answer
    
#199 Binary tree right side view. Do the same BFS as Binary tree level order traversal, but only return the last value of each level
class RightSideView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)

            level = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if level:
                answer.append(level[-1])
        
        return answer
    

# 1448. Count nodes in tree which don't have any parent nodes greater than them. Dfs, passing along max value to each recursive call
class GoodNodes:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode, maxValue: int) -> int:
            if not node:
                return 0
            
            res = 0
            if node.val >= maxValue:
                res += 1
            
            maxValue = max(maxValue, node.val)
            
            res += dfs(node.left, maxValue)
            res += dfs(node.right, maxValue)

            return res

        return dfs(root, root.val)
    


        