"""
Find Closest Value In BST
<p>You can assume that there will only be one closest value.</p>
<p>
  Each BST node has an integer value, a
  left child node, and a right child node. A node is
  said to be a valid BST node if and only if it satisfies the BST
  property: its value is strictly greater than the values of every
  node to its left; its value is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  BST nodes themselves or None / null.
</p>

"""
from bst import BST

# def findClosestValueInBst(tree, target: int):
#     return findClosestValueInBst_help(tree, target, tree.value)


# def findClosestValueInBst_help(tree, target: int, closest: float):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     if target < tree.value:
#         return findClosestValueInBst_help(tree.left, target, closest)
#     else:
#         return findClosestValueInBst_help(tree.right, target, closest)
def findClosestValueInBst(tree, target: int):
    closest = tree.value
    cur_node: BST = tree

    while cur_node:
        if abs(target - closest) > abs(target - cur_node.value):
            closest = cur_node.value
        if cur_node.value < target:
            cur_node = cur_node.right
        else:
            cur_node = cur_node.left
    return closest






def main():    
    t = BST(10)
    t = t.insert(15).insert(13).insert(22).insert(14).insert(5).insert(5).insert(2).insert(1)
    print(findClosestValueInBst(t, 12))

if __name__ == "__main__":
    main()
