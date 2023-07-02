"""
BST Construction
<p>
  Write a BST class for a Binary Search Tree. The class should support:
</p>
<ul>
  <li>Inserting values with the insert method.</li>
  <li>
    Removing values with the remove method; this method should only remove the first instance of a given value.
  </li>
  <li>Searching for values with the contains method.</li>
</ul>
<p>
  Note that you can't remove values from a single-node tree. In other words,
  calling the remove method on a single-node tree should simply not
  do anything.
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
Hint 1 
<p>
As you try to insert, find, or a remove a value into, in, or from a BST, you will have to traverse the tree's nodes. 
The BST property allows you to eliminate half of the remaining tree at each node that you traverse: 
if the target value is strictly smaller than a node's value, then it must be (or can only be) located to the left of the node, 
otherwise it must be (or can only be) to the right of that node.
</p>
Hint 2
<p>
Traverse the BST all the while applying the logic described in Hint #1. 
For insertion, add the target value to the BST once you reach a leaf (None / null) node. 
For searching, if you reach a leaf node without having found the target value that means the value isn't in the BST. 
For removal, consider the various cases that you might encounter: 
    the node you need to remove might have two children nodes, one, or none; 
    it might also be the root node; make sure to account for all of these cases.
</p>
Hint 3
<p>
What are the advantages and disadvantages of implementing these methods iteratively as opposed to recursively?
</p>

Average (all 3 methods): O(log(n)) time | O(1) space - where n is the number of nodes in the BST
Worst (all 3 methods): O(n) time | O(1) space - where n is the number of nodes in the BST
"""

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        return self

    def contains(self, value):
        # if value == None:
        #     return False
        
        if value == self.value:
            return True
        
        if value < self.value:
            if self.left:
                return self.left.contains(value)
            else:
                return False
        
        else:
            if self.right:
                return self.right.contains(value)
            else:
                return False
                

    def remove(self, value, parent=None):
        current_nodee = self
        while current_nodee is not None:
            if value < current_nodee.value:
                parent = current_nodee
                current_nodee = current_nodee.left
            elif value > current_nodee.value:
                parent = current_nodee
                current_nodee = current_nodee.right
            else:
                if current_nodee.left is not None and current_nodee.right is not None:
                    current_nodee.value = current_nodee.right.get_min_node()
                    current_nodee.right.remove(current_nodee.value, current_nodee)
                # root 
                elif parent is None:
                    if current_nodee.left is not None:
                        current_nodee.value = current_nodee.left.value
                        current_nodee.right = current_nodee.left.right
                        current_nodee.left = current_nodee.left.left
                    elif current_nodee.right is not None:
                        current_nodee.value = current_nodee.right.value
                        current_nodee.right = current_nodee.right.right
                        current_nodee.left = current_nodee.right.left
                    else:
                        # only root node in the tree
                        # current_nodee.value = None
                        return 

                elif parent.left == current_nodee:
                    parent.left = current_nodee.left if current_nodee.left is not None else current_nodee.right
                elif parent.right == current_nodee:
                    parent.right = current_nodee.left if current_nodee.left is not None else current_nodee.right
                break
        return self

    

    def get_min_node(self):
        cur_node = self
        while cur_node.left is not None:
            cur_node = cur_node.left
        return cur_node.value
    
def main():    
    t = BST(10)
    t = t.insert(5).insert(15)
    t.remove(5)
    t.remove(15)
    t.remove(10)
    print(t.value)

if __name__ == "__main__":
    main()


