Problem link : - https://leetcode.com/problems/two-sum-iv-input-is-a-bst/


Approach : - Do the In order Traversal of BST & will get Sorted array as a output, use the res array to check if sum exist
Note : - Memory complexity can be reudced by using two pointer approach

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = [] 
        dict = {}
        
        def Inorder(root):
            if not root:
                return        
            Inorder(root.left)
            res.append(root.val)
            Inorder(root.right)
        Inorder(root)
        
        for index, ele in enumerate(res):
            if k - ele in dict:
                return True
            dict[ele] = index
        return False
