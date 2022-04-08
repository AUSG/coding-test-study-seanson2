class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r1, r2):
            if r1 is None and r2 is None:
                return
            if r1 is None:
                return TreeNode(r2.val, r2.left, r2.right)
            elif r2 is None:
                return TreeNode(r1.val, r1.left, r1.right)
            else:
                return TreeNode(r1.val+r2.val, dfs(r1.left, r2.left), dfs(r1.right, r2.right))

        return dfs(root1, root2)
