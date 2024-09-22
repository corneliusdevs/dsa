class BinaryNode:
    def __init__(self, data:any):
        self.data = data
        self.leftNode = None
        self.rightNode = None


# 2. IN-ORDER TREE TRAVERSAL. It is called In-Order because it prints the values in ascending order in a binary search tree. It first does a recursive In-order tree traversal of the left sub-tree, visits the root node and then does a recursive In-order tree traversal of the right subtree.
# What makes it special is that it prints all the values of the left sub-tree, then the value of the parent node before all the values of the right sub-tree
# left sub-tree -> parent node -> right subtree 
# It is mainly used in Binary search trees where it returns values in ascending order
# Major difference code wise is that the print statement is located after the In-order tree traversal of the left sub-tree

def in_order_tree_traversal(node:BinaryNode):
    if(node is None):
        return
    in_order_tree_traversal(node.leftNode)
    print(node.data, end=" , ")
    in_order_tree_traversal(node.rightNode)