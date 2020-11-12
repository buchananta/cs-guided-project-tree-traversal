"""
You are given a binary tree.

Write a function that can return the inorder traversal of node values.

Example:
Input:

   3
    \
     1
    /
   5

Output: [3,5,1]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    # Your code here

#pre-order depth-first
def iter_depth_first_traverse(root):
    result = []
    stack = []
    if root is None:
        return result
    stack.append(root)

    while len(stack) != 0:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def iter_pre_order_traverse(root):
    result = []
    queue = deque()
    if root is None:
        return result
    queue.appendleft(root)

    