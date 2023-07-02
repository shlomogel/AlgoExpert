# class BinaryTree:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
from __init__ import BT

def evaluateExpressionTree(tree):
    if tree.value >= 0 :
        return tree.value
    
    if tree.value == -1:
        return evaluateExpressionTree(tree.left) + evaluateExpressionTree(tree.right)
    if tree.value == -2:
        return evaluateExpressionTree(tree.left) - evaluateExpressionTree(tree.right)
    if tree.value == -3:
        return int(evaluateExpressionTree(tree.left) / evaluateExpressionTree(tree.right))
    if tree.value == -4:
        return evaluateExpressionTree(tree.left) * evaluateExpressionTree(tree.right)



bt = BT(-1)
bt.insert(-2)
bt.insert(-3)
bt.insert(-4)
bt.insert(2)
bt.insert(8)
bt.insert(3)
bt.insert(2)
bt.insert(3)


t = evaluateExpressionTree(bt)
print(t)
