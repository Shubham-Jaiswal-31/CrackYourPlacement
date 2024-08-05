# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        def generate(l, r):
            if l > r:
                return [None]
            if (l, r) in dp:
                return dp[(l, r)]
            res = []
            for val in range(l, r + 1):
                for leftTree in generate(l, val - 1):
                    for rightTree in generate(val + 1, r):
                        root = TreeNode(val, leftTree, rightTree)
                        res.append(root)
            dp[(l, r)] = res
            return res
        return generate(1, n)