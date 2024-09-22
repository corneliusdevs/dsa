class BinaryNode:
    def __init__(self, data:any):
        self.data = data
        self.leftNode = None
        self.rightNode = None




#  DEPTH FIRST TREE TRAVERSAL
# 1. PRE ORDER TREE TRAVERSAL. It is called pre-order tree traversal because the node is visited first before the recursive pre-order tree traversal of the left or right node

def pre_order_traversal(node:BinaryNode):
    if(node is None):
        return
    
    print(node.data, end=" , ")
    pre_order_traversal(node.leftNode)
    pre_order_traversal(node.rightNode)

