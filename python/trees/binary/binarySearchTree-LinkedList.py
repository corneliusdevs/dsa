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
        if(rootNode is None or nodeToInsert is None):
            return
        elif rootNode.data == nodeToInsert.data:
            # if the node is already in the tree return
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
    
    def getNodeToDelete(self, parentNode:BinaryTreeNode, nodeToDelete: BinaryTreeNode, nodeBeforeNodeToBeDeleted:BinaryTreeNode | None) -> tuple[BinaryTreeNode | None, BinaryTreeNode | None]:
        """The Method returns a tuple in the format (nodeToDelete, nodeBeforeTheNodeToBeDeleted)"""
        if parentNode.data == nodeToDelete.data:
            return [nodeToDelete, nodeBeforeNodeToBeDeleted]
        
        if nodeToDelete.data < parentNode.data:
            # if there is no left node, it means the nodeToDelete is not in the tree
            if parentNode.leftNode is None:
                # return an empty tuple
                return ()
            
            return self.getNodeToDelete(parentNode.leftNode, nodeToDelete, parentNode)
        
        elif nodeToDelete.data > parentNode.data:
            # if there is no right node, it means we have reached the end of the tree and the nodeToDelete is not in the tree
            if parentNode.rightNode is None:
                # return an empty tuple
                return ()
            
            return self.getNodeToDelete(parentNode.rightNode, nodeToDelete, parentNode)
        
        return ()
    
    def  isInRightSubTree(self, parentNode:BinaryTreeNode, node):
          if(parentNode == None):
              return None
          return parentNode.rightNode == node
        
    
    def deleteNode(self, rootNode:BinaryTreeNode, nodeTodelete:BinaryTreeNode) -> BinaryTreeNode:
        """This function deletes a node from a binary tree and returns the root node"""

        if(nodeTodelete is None):
            return rootNode
        
        (_, parentNode) = self.getNodeToDelete(rootNode, nodeTodelete, None)

        leftOfNodeToBeDeleted = nodeTodelete.leftNode
        rightOfNodeToBeDeleted = nodeTodelete.rightNode

        
        isInRightSubTreeOfParentNode = self.isInRightSubTree(parentNode, nodeTodelete)
        isInLeftSubTreeOfParentNode = isInRightSubTreeOfParentNode == False

        # checks if Node to be deleted is a leaf Node
        nodeTodeleteIsLeafNode = (leftOfNodeToBeDeleted == None) == (rightOfNodeToBeDeleted == None)

        if(parentNode):
            if(isInLeftSubTreeOfParentNode):
                if(rightOfNodeToBeDeleted is not None):
                    newChildOfParent = rightOfNodeToBeDeleted
                    parentNode.leftNode = newChildOfParent
                    # insert the left sub tree in a suitable position in the binary tree following the rules of inserting a new node in a binary search tree
                    self.insertNode(newChildOfParent, leftOfNodeToBeDeleted)

                elif leftOfNodeToBeDeleted is not None:
                    newChildOfParent = leftOfNodeToBeDeleted
                    parentNode.leftNode = newChildOfParent

                elif nodeTodeleteIsLeafNode :
                    # if this runs, it means the nodeToDelete is a leaf node: this means that it does not have a left node or a right node

                    # because we are sure that we are in the left sub tree of the parent node we set the leftNode of the parent Node to be equal to none
                    parentNode.leftNode = None
                else:
                    parentNode.leftNode = None


            elif(isInRightSubTreeOfParentNode):
                if(rightOfNodeToBeDeleted is not None):
                    newChildOfParent = rightOfNodeToBeDeleted
                    parentNode.rightNode = newChildOfParent
                    # insert the left sub tree in a suitable position in the binary tree following the rules of inserting a new node in a binary search tree
                    self.insertNode(newChildOfParent, leftOfNodeToBeDeleted)

                elif leftOfNodeToBeDeleted is not None:
                    newChildOfParent = leftOfNodeToBeDeleted
                    parentNode.rightNode = newChildOfParent

                elif nodeTodeleteIsLeafNode :
                    # if this runs, it means the nodeToDelete is a leaf node: this means that it does not have a left node or a right node

                    # because we are sure that we are in the left sub tree of the parent node we set the leftNode of the parent Node to be equal to none
                    parentNode.rightNode = None
                else:
                    parentNode.rightNode = None
            
        elif parentNode is None:
            # It means the node we want to delete is most likely a root node because it does not have a parent node
            
            if nodeTodelete.rightNode is None:
                # set the left of the nodeToDelete as the new root node
                rootNode = nodeTodelete.leftNode
            elif nodeTodelete.leftNode is None :
                # set the right of the nodeToDelete as the new root node
                rootNode = nodeTodelete.rightNode 
            else:
                # if we run this block, it means that the nodeToDelete has left and right nodes or subTrees
                pass
                
                # make the right node the new root node
                rootNode = nodeTodelete.rightNode

                # insert the left sub tree in a suitable position in the binary tree following the rules of inserting a new node in a binary search tree
                self.insertNode(rootNode, nodeTodelete.leftNode)

        
        # dis-associate the nodeToBeDeleted from the tree
        nodeTodelete.leftNode = None
        nodeTodelete.rightNode = None 

        return rootNode
                

        
            

        



# ------- MANUALLY CREATE THE NODES AND INSERT THE VALUES AND LINK THEM  ------
# first create the rootNode
rootNode = BinaryTreeNode(13)

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


# # perform in_order_tree_traversal
# print("in order traversal ") 
# binarySearchTreeMethods.in_order_traversal(rootNode) # Note that the values are printed in ascending order

# # perform pre_order_tree_traversal
# print("\npre order traversal ")
# binarySearchTreeMethods.pre_order_traveral(rootNode)

# # perform pre_order_tree_traversal
# print("\npost order traversal ")
# binarySearchTreeMethods.post_order_traversal(rootNode)

# # print the lowest value in the tree
# print("\nlowest value in tree is: ", binarySearchTreeMethods.print_lowest_value_in_tree(rootNode))


# Insert a node
node2 = BinaryTreeNode(2)
node1 = BinaryTreeNode(1)
node100 = BinaryTreeNode(100)

# print("\ninserting node ")
# binarySearchTreeMethods.insertNode(rootNode, node100)
# # perform in_order_tree_traversal
# print("in order traversal ") 
# binarySearchTreeMethods.in_order_traversal(rootNode) # Note that the values are printed in ascending order

# # print the lowest value in the tree
# print("\nlowest value in tree is: ", binarySearchTreeMethods.print_lowest_value_in_tree(rootNode))
# # print the lowest value in the tree
# print("\nHighest value in tree is: ", binarySearchTreeMethods.print_highest_value_in_tree(rootNode))

print("\ndeleting node ")
binarySearchTreeMethods.in_order_traversal(rootNode)
newRootNode = binarySearchTreeMethods.deleteNode(rootNode, node19)
print("\n traversing node")
binarySearchTreeMethods.in_order_traversal(newRootNode)


# ------ AUTOMATICALLY CREATE A NEW NODE AND INSERT THE NODE IN THE TREE ------
