class BSTNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    #base case(s)
    #we realize we need to go in a direction, bu there's no node in said directoin
    #we can put the value in this spot
    #how we getcloser to the base case
    if value < self.value:
      #go left
      #check there is a child node in the left direction
      if self.left is None:
        self.left = BSTNode(value)
      else:
        #move left down the tree
        self.left.insert(value)
    #duplicates go on the right
    else:
      #go right
      if self.right is None:
        self.right = BSTNode(value)
      else:
        #move right down the tree
        self.right.insert(value)
    
  def search(self, target):
    #base case(s)
    #1. We found what we're looking for
    if self.value == target:
      return self
    elif target < self.value:
      #2. We've looked through where the element must be if it existed but didnt find it
      if self.left is None:
        return False
      else:
        #we need to go left
        #do so by calling the left child's `search` method
        return self.left.search(target)
    else:
      #go right
      if self.right is None:
        return False
      else:
        # we need to go right
        # we do so by calling the right child's `search` method
        return self.right.search(target)

bst = BSTNode(35)
bst.insert(18)
bst.insert(47)
bst.insert(14)
bst.insert(22)
bst.insert(35)
bst.insert(55)