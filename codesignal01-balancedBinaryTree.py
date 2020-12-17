#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def balancedBinaryTree(root):
    if root is None:
        return True
    
    # print(root.value)
    left_height = findMaxHeight(root.left)
    right_height = findMaxHeight(root.right)
    
    if abs(left_height - right_height) <= 1:
        if balancedBinaryTree(root.left) and balancedBinaryTree(root.right):
            return True
        else:
            return False
    else:
        return False

def findMaxHeight (root):
    if root is None:
        return 0
    
    left_height = findMaxHeight(root.left)
    
    right_height = findMaxHeight(root.right)
    
    return max(left_height, right_height) + 1
    
    