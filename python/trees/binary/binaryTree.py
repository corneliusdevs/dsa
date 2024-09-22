
class BinaryNode:
    def __init__(self, data:any):
        self.data = data
        self.leftNode = None
        self.rightNode = None

rootNode = BinaryNode("R")
nodeA = BinaryNode("A")
nodeB = BinaryNode("B")
nodeC = BinaryNode("C")
nodeD = BinaryNode("D")
nodeE = BinaryNode("E")
nodeF = BinaryNode("F")
nodeG = BinaryNode("G")
nodeH = BinaryNode("H")

rootNode.leftNode = nodeA
rootNode.rightNode = nodeB

nodeA.leftNode = nodeC
nodeA.rightNode = nodeD

nodeB.leftNode = nodeE
nodeB.rightNode = nodeF

nodeF.leftNode = nodeG

print("rootNode.rightNode.leftNode.data: ", rootNode.rightNode.leftNode.data)

#  DEPTH FIRST TREE TRAVERSAL
# 1. PRE ORDER TREE TRAVERSAL. It is called pre-order tree traversal because the node is visited first before the recursive pre-order tree traversal of the left or right node

def pre_order_traversal(node:BinaryNode):
    if(node is None):
        return
    
    print(node.data, end=" , ")
    pre_order_traversal(node.leftNode)
    pre_order_traversal(node.rightNode)

print("\npre-order traversal")
pre_order_traversal(rootNode)

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

print("\nIn-order traversal")
in_order_tree_traversal(rootNode)


# POST-ORDER TREE TRAVERSAL
# It is done by doing a post-order tree traversal of the left nodes, followed by a post-order tree traversal of the right nodes before visiting the root node. Hence the value stored at the root node will always be the last output in the post-order-tree traversal.
# Notice that the print statement is placed after the post-order tree traversal of the left and right sub-trees

def post_order_tree_traversal(node:BinaryNode):
    if(node is None):
        return
    
    post_order_tree_traversal(node.leftNode)
    post_order_tree_traversal(node.rightNode)
    print(node.data, end=" , ")

print("\nPost-order traversal")
post_order_tree_traversal(rootNode)
