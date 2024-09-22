class BinaryNode:
    def __init__(self, data:any):
        self.data = data
        self.leftNode = None
        self.rightNode = None


# POST-ORDER TREE TRAVERSAL
# It is done by doing a post-order tree traversal of the left nodes, followed by a post-order tree traversal of the right nodes before visiting the root node. Hence the value stored at the root node will always be the last output in the post-order-tree traversal.
# Notice that the print statement is placed after the post-order tree traversal of the left and right sub-trees

def post_order_tree_traversal(node:BinaryNode):
    if(node is None):
        return
    
    post_order_tree_traversal(node.leftNode)
    post_order_tree_traversal(node.rightNode)
    print(node.data, " , ")

print("\nPost-order traversal")