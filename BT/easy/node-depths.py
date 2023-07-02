"""
Node Depths
<p>
  The distance between a node in a Binary Tree and the tree's root is called the
  node's depth.
</p>
<p>
  Write a function that takes in a Binary Tree and returns the sum of its nodes'
  depths.
</p>
"""
from __init__ import binary_tree

def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


print(nodeDepths(binary_tree))