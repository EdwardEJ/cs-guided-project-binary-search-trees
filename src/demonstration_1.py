"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(root):
  '''
  Input: root node of the binary tree we want to find the max depth for
  Output: Integer representing the max depth

  Base case: Check a node, if there's nothing there, there's a depth of 0
  How do we move closer to the base case?

  Recurse in both its left and right directions
  Both recursive calls are going to come back with answers from further down the tree
  We'll need to get the max of those returns values and the add 1 to account forthe current node itself
  
  '''
  #checking if the current is is not Empty
  if root is None:
    return 0
  #the root node is not empty
  #recurse on the left and right sides
  #to find their respective depths
  left_height = maxDepth(root.left)
  right_height = maxDepth(root.right) 
  # add 1 to account for this current node
  return max(left_height, right_height) + 1