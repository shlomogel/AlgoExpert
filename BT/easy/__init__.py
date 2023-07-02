class BT:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        tree = self
        queue = [tree]

        while queue:
            curr_node = queue.pop(0)

            if curr_node.left is None:
                curr_node.left = BT(value)
                break
            else:
                queue.append(curr_node.left)
            
            if curr_node.right is None:
                curr_node.right = BT(value)
                break
            else:
                queue.append(curr_node.right)

binary_tree = BT(10)
binary_tree.insert(20)
binary_tree.insert(30)
binary_tree.insert(40)
binary_tree.insert(50)
binary_tree.insert(60)

   


                
