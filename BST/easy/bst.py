
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


