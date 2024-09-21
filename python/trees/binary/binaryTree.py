
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

nodeC.leftNode = nodeG
nodeC.rightNode = nodeH

print("rootNode.rightNode.leftNode.data: ", rootNode.rightNode.leftNode.data)

# PRE ORDER TREE TRAVERSAL. It is called pre-order tree traversal because the node is visited first before the recursive pre-order tree traversal of the left or right node

