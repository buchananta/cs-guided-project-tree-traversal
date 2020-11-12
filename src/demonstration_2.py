"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and output a binary tree.

*Note: assume that there will not be any duplicates in the tree.*

Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]

Output:
    5
   / \
  7  22
    /  \
   13   9
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    # Your code here
    preorder_index = 0
    root = TreeNode(preorder[preorder_index]) 
    
    inorder_index_map = {}

    for i, elem in enumerate(inorder):
        inorder_index_map[elem] = i
        
    return recurse(preorder, preorder_index, inorder_index_map)

def recurse(preorder, proorder_index, inorder_index_map):
    if inorder_start > inorder_end:
        return  