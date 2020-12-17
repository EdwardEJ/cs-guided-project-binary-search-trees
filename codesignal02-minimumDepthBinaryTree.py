def minimumDepthBinaryTree(root):
    if root is None:
        return 0
        
    if root.right is None:
        return minimumDepthBinaryTree(root.left) + 1
        
    if root.left is None:
        return minimumDepthBinaryTree(root.right) + 1
        
    left_depth = minimumDepthBinaryTree(root.left)
    right_depth = minimumDepthBinaryTree(root.right)
    
    return min(left_depth, right_depth) + 1
          