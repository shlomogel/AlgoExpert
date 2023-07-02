"""
Branch Sums

<p>
  Write a function that takes in a Binary Tree and returns a list of its branch
  sums ordered from leftmost branch sum to rightmost branch sum.
</p>
<p>
  A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree
  branch is a path of nodes in a tree that starts at the root node and ends at
  any leaf node.
</p>
<p>
  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or
  None / null.
</p>
Hint 1 
<p>
  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or
  None / null.
</p>
Hint 2
<p>
Recursively traverse the Binary Tree in a depth-first-search-like fashion, 
and pass a running sum of the values of every previously-visited node to each node that you're traversing.
</p>
Hint 3
<p>
As you recursively traverse the tree, 
if you reach a leaf node (a node with no "left" or "right" Binary Tree nodes), 
add the relevant running sum that you've calculated to a list of sums 
(which you'll also have to pass to the recursive function). 
If you reach a node that isn't a leaf node, keep recursively traversing its children nodes, 
passing the correctly updated running sum to them.
</p>
"""
import __init__ as BT


def branchSums(root):
    if root is None:
        return []
    branch_sums = branchSums(root.left) + branchSums(root.right)
    if not branch_sums:
        return [root.value]
    else:
        return [x + root.value for x in branch_sums]


print(branchSums(BT.binary_tree))




