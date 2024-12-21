class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree_Methods:
    def getHeight(self, node:TreeNode):
        if not node:
            return 0
        return node.height

    def getBalance(self, node:TreeNode):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def rightRotate(self, y:TreeNode):
        print('rotate right on node', y.data)
        x:TreeNode = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x
    
    def leftRotate(self, x:TreeNode):
        print('Rotate left on node', x.data)
        y:TreeNode = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    def insert(self, node:TreeNode, data):
        if not node:
            return TreeNode(data)
        
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        # update the balance factor and balance the tree
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        balance = self.getBalance(node)

        # balancing the tree
        # Left Left balancing
        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rightRotate(node)
        
        # Right Right balancing
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        
        # Right Left balancing
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.leftRotate(node)
        
        # Right Left
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        
        return node
    
    def in_order_traversal(self, node:TreeNode):
        if node is None:
            return
        
        self.in_order_traversal(node.left)
        print(node.data, end=", ")
        self.in_order_traversal(node.right)

    def minValue(self, node:TreeNode):
        """This function will return the minimum value of the tree given a node as a rootNode"""
        current = node
        while current.left is not None:
            current = current.left
        return current


    def delete(self, node:TreeNode, data):
        # first find the node to be deleted
        if not node:
            return node
        
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)

        else:
            # It means that node.data == data and we are at the node we want to delete
            # check if the node we want to delete has a child left node or not
            if node.left == None:
                temp = node.right # temporary store the value of the right node
                node = None
                # return the right node as the child node of the node above it
                return temp
            
            if node.right == None:
                temp = node.left
                # delete the node by setting it to none
                node = None
                return temp
        
            # if we run this block, it means that the node to be deleted has both left and right node so we:
            # find the in-order successor of the node, relace the current value of this node with the value of the in-order sucessor and delete the in-order sucessor
            # Note that since it is an AVL tree, the maximum height of a node is 1, so the in-order successor will always end up being a leaf node and we will be deleting a leaf node

            inOrderSuccessor = self.minValue(node.right) # in-order succesor is the minimum value of the right subtree of the node
            node.data = inOrderSuccessor.data # swap out the data of the inOrderSuccesor and the node

            # delete the inorder succesor and assign the retuned node to the node.right. Take the node.right as the rootNode to start the deletion from, use the in-order succesor's data to locate the node and delete it. You should be deleting a keaf node and returning the right subtree which should be none or a node as the new node.right
            node.right = self.delete(node.right, inOrderSuccessor.data)


        #  This is a guard clause to prevent us from evaluating the following lines of code if the node is none
        if node is None:
            return None
        
        # If the node is not none, let us calculate the tree height of this node and balance the node before returning.
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        balance = self.getBalance(node)

        # let us balance node tree using either:
        #  Left Left rotation if the node and the left child node are both left heavy
        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rightRotate(node)
        
        # else, let us do a Left Right rotation if the node is left heavy but the left child node is right heavy
        if balance > 1 and self.getBalance(node.left) < 0:
            # perform a left rotation of the left child node first
            node.left = self.leftRotate(node.left)
            # perform a right rotation on the node
            return self.rightRotate(node)
        
        # else let us do a Right Right rotation if the node is Right heavy and its right node is right heavy
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.leftRotate(node)
        
        # else let us do a Right Left rotation if the node is right heavy but the right child node is left heavy
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        
        #  when you have deleted, updated the height of and balanced the node, return it

        return node


    def createAnddeleteTreeFromArray(self, array:list):
        if not list:
            array = ["C", "B", "E", "A", "D", "H", "G", "F"]
        root = None
        for letter in array:
            root = self.insert(root, letter)
        self.in_order_traversal(root)
        print("\nDeleting A")
        root = self.delete(root, 'A')
        self.in_order_traversal(root)


avlTree =  AVL_Tree_Methods()
avlTree.createAnddeleteTreeFromArray(["C", "B", "E", "A", "D", "H", "G", "F"])



# -----       STEPS FOR DELETION OF AN AVL NODE ----- 
# Step 1: Firstly, find that node where k is stored

# Step 2: Secondly, delete those contents of the node (Suppose the node is x)

# Step 3: Claim: Deleting a node in an AVL tree can be reduced by deleting a leaf. There are three possible cases:

# When x has no children, then delete x
# When x has one child, let x' becomes the child of x.
# Notice: x' cannot have a child since subtrees of T can differ in height by at most one :
# then replace the contents of x with the contents of x'
# then delete x' (a leaf)
# Step 4:  When x has two children,
# then find x's successor z (which has no left child)
# then replace x's contents with z's contents, and
# delete z
# In all three cases, you will end up removing a leaf.

