#Time Complexity : O(n)
#Space Complexity : O(height of k)
#Did this code successfully run on Leetcode : Yes
#youtube : https://youtu.be/6yzbNapzqcY
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #maintaing count for checking the value of k 
    count = 0
    result = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #doing inorder traversal
        self.helper(root, k)
        return self.result
    
    def helper(self, root, k):
        #base condition
        if root == None:
            return 

        #logic
        #checking the left child first 
        self.helper(root.left, k)
        self.count = self.count + 1
        #if we find count is equal to k then we will set the value of result
        if self.count == k:
            self.result = root.val
        #checking the right child
        self.helper(root.right, k)
        
#followup in readme
