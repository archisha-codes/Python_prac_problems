# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # hashmap for fast lookup
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        self.pre_index = 0
        
        def helper(left, right):
            if left > right:
                return None
            
            # pick root from preorder
            root_val = preorder[self.pre_index]
            self.pre_index += 1
            
            root = TreeNode(root_val)
            
            # split inorder
            mid = inorder_map[root_val]
            
            # build left and right subtree
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        
        return helper(0, len(inorder) - 1)