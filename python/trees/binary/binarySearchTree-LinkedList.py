#  This is a linked list implementation of a BINARY SEARCH TREE. 
#  Each node has a right and left node.
#  Each node links to another node that can have a right and a left node.
#  Values lower than the Node value are inserted to the left of the node.
#  Values higher than the Node value are inserted to the right of the node

# 1. Define the node class First
class BinaryTreeNode:
    def __init__(self, data:any):
        self.data = data
        self.leftNode = None
        self.rightNode = None


#  implement methods of traversing the nodes, deleting a node, searching for a value and searching for the lowest value

class BinarySearchTreeMethods:
    def in_order_traversal(self, node:BinaryTreeNode):
        if(node is None):
            return
        self.in_order_traversal(node.leftNode)
        print(node.data, end=", ")
        self.in_order_traversal(node.rightNode)

    def pre_order_traveral(self, node:BinaryTreeNode):
        if(node is None):
            return
        print(node.data, end=", ")
        self.pre_order_traveral(node.leftNode)
        self.pre_order_traveral(node.rightNode)

    def post_order_traversal(self, node:BinaryTreeNode):
        if(node is None):
            return 
        self.post_order_traversal(node.leftNode)
        self.post_order_traversal(node.rightNode)
        print(node.data, end=", ")

    def print_lowest_value_in_tree(self, node: BinaryTreeNode):
        """The Method assumes that the Binary Search tree is well sorted and Obeys the Laws of an actual Binary Search Tree. Make sure to pass the rootNode as the argument to the function when it is called"""
        if(node.leftNode is None):
            return node.data
        
        nextNodeData = node.leftNode.data
        currentNodeData = node.data
        if(nextNodeData > currentNodeData):
            return currentNodeData

        return self.print_lowest_value_in_tree(node.leftNode)
    
    def print_highest_value_in_tree(self, node:BinaryTreeNode):
        """The Method assumes that the Binary Search tree is well sorted and Obeys the Laws of an actual Binary Search Tree. Make sure to pass the rootNode as the argument to the function when it is called"""
        if(node.rightNode is None):
            return node.data
        currentNodeData = node.data
        nextNodeData = node.rightNode.data
        if(nextNodeData < currentNodeData):
            return currentNodeData
        
        return self.print_highest_value_in_tree(node.rightNode)

    def insertNode(self, rootNode:BinaryTreeNode, nodeToInsert:BinaryTreeNode):
        # if value is already in the tree, return
        if rootNode.data == nodeToInsert.data:
            return 

        if nodeToInsert.data < rootNode.data:
            if(rootNode.leftNode is None):
                rootNode.leftNode = nodeToInsert
                return
            return self.insertNode(rootNode.leftNode, nodeToInsert)
            

        if nodeToInsert.data > rootNode.data :
            if(rootNode.rightNode is None):
                rootNode.rightNode = nodeToInsert
                return
            return self.insertNode(rootNode.rightNode, nodeToInsert)
        
        return
            
        
            

        



# ------- MANUALLY CREATE THE NODES AND INSERT THE VALUES AND LINK THEM  ------
# first create the rootNode
rootNode = BinaryTreeNode(150)

# create the node
node7 = BinaryTreeNode(7)
node15 = BinaryTreeNode(15)
node3 = BinaryTreeNode(3)
node8 = BinaryTreeNode(8)
node14 = BinaryTreeNode(14)
node19 = BinaryTreeNode(19)
node18 = BinaryTreeNode(18)

# --- Link the nodes making sure lower values are inserted on left nodes and higher values on right nodes ---
rootNode.leftNode = node7
rootNode.rightNode = node15

node7.leftNode = node3
node7.rightNode = node8

node15.leftNode = node14
node15.rightNode = node19

node19.leftNode = node18

# Create a BinarySearchTree Object so that you can use its methods to search the binaryTree Just created
binarySearchTreeMethods = BinarySearchTreeMethods()

# perform in_order_tree_traversal
print("in order traversal ") 
binarySearchTreeMethods.in_order_traversal(rootNode) # Note that the values are printed in ascending order

# perform pre_order_tree_traversal
print("\npre order traversal ")
binarySearchTreeMethods.pre_order_traveral(rootNode)

# perform pre_order_tree_traversal
print("\npost order traversal ")
binarySearchTreeMethods.post_order_traversal(rootNode)

# print the lowest value in the tree
print("\nlowest value in tree is: ", binarySearchTreeMethods.print_lowest_value_in_tree(rootNode))


# Insert a node
node2 = BinaryTreeNode(2)
node1 = BinaryTreeNode(1)
node100 = BinaryTreeNode(100)

print("\ninserting node ")
binarySearchTreeMethods.insertNode(rootNode, node100)
# perform in_order_tree_traversal
print("in order traversal ") 
binarySearchTreeMethods.in_order_traversal(rootNode) # Note that the values are printed in ascending order

# print the lowest value in the tree
print("\nlowest value in tree is: ", binarySearchTreeMethods.print_lowest_value_in_tree(rootNode))
# print the lowest value in the tree
print("\nHighest value in tree is: ", binarySearchTreeMethods.print_highest_value_in_tree(rootNode))

# ------ AUTOMATICALLY CREATE A NEW NODE AND INSERT THE NODE IN THE TREE ------
