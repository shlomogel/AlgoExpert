"""
Validate BST
<p>
  Write a function that takes in a potentially invalid Binary Search Tree (BST)
  and returns a boolean representing whether the BST is valid.
</p>
<p>
  Each BST node has an integer value, a
  left child node, and a right child node. A node is
  said to be a valid BST node if and only if it satisfies the BST
  property: its value is strictly greater than the values of every
  node to its left; its value is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  BST nodes themselves or None / null.
</p>
<p>
  A BST is valid if and only if all of its nodes are valid
  BST nodes.
</p>
Hint 1
<p>
Every node in the BST has a maximum possible value and a minimum possible value. In other words, the value of any given node in the BST must be strictly smaller than some value (the value of its closest right parent) and must be greater than or equal to some other value (the value of its closest left parent).
</p>
Hint 2
<p>
Validate the BST by recursively calling the validateBst function on every node, passing in the correct maximum and minimum possible values to each. Initialize those values to be -Infinity and +Infinity.
</p>
O(n) time | O(d) space - where n is the number of nodes in the BST and d is the depth (height) of the BST

"""
from bst import BST
# This is an input class. Do not edit.


def validateBst(tree: BST, min:float=float("-inf"), max:float=float("inf")):
    if tree is None:
        return True
    if tree.value < min or tree.value >= max:
        return False
    return validateBst(tree=tree.left, min=min, max=tree.value) and \
        validateBst(tree=tree.right, min=tree.value, max=max)

def main():    
    t = BST(10)
    t = t.insert(15).insert(5).insert(6)
    t.left.right.value = 10
    print(validateBst(t))

if __name__ == "__main__":
    main()