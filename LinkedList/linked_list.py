
from typing import Any, List, Union

class EmptyList(Exception):
    def __init__(self, message="List is empty"):
        self.message = message
        super().__init__(self.message)


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            self.head = Node(data=nodes[0])
            current = self.head
            for node_data in nodes[1:]:
                current.next = Node(data=node_data)
                current = current.next



    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def get_node(self, node:Node):
        for n in self:
            if n.data == node.data:
                return n
        raise IndexError(f'{node.data} Not Found!')
    
    def exists(self, node:Node):
        for n in self:
            if n.data == node.data:
                return True
        return False


    def add_first(self, node: Node):
        node.next = self.head
        self.head = node

    def add_last(self, node:Node):
        if self.head is None:
            self.head = node
            return
        # iterate over the list till the end
        for cur_node in self:
            pass
        cur_node.next = node

    def add_after(self, new_node:Node, after:Any):
        if self.head is None:
            raise EmptyList()
        for n in self:
            if n.data == after:
                new_node.next = n.next
                n.next = new_node
                return        
        raise IndexError(f'{after} Not Found!')
    
    def add_before(self, new_node:Node, before:Any):
        if self.head is None:
            raise EmptyList()
        prev = self.head
        for n in self:
            if n.data == before:
                new_node.next = n
                prev.next = new_node
                return
            prev = n        
        raise IndexError(f'{before} Not Found!')
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise EmptyList()
        
        prev_node = self.head

        for current_node in self:
            if current_node.data == target_node_data:
                prev_node.next = current_node.next
                return 
            prev_node = current_node
        
        raise IndexError(f'{target_node_data} Not Found!')


# def findLoop(head):
#     slow_r, fast_r = head, head
    
#     while fast_r:
#         slow_r = slow_r.next
#         fast_r = fast_r.next.next

#         if slow_r is fast_r:
#             break

#     p = head
#     while p is not fast_r:
#         p = p.next
#         fast_r = fast_r.next
        
#     return p
