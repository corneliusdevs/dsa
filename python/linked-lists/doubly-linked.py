
# define Node class
class Node:
    def __init__(self, data:int):
        self.data = data
        self.prevNode:'Node' = None
        self.nextNode:'Node' = None

# create the objects
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# link the nodes forwards
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

# link the nodes backwards
node4.prevNode = node3
node3.prevNode = node2
node2.prevNode = node1


def printNodeValueForwards(headNode):
    print("traversing forwards")
    print(headNode.data, end=" => ")
    currentNode = headNode.nextNode
    startNode = headNode
    while (currentNode and currentNode != startNode):
        print(currentNode.data, end=" => ")
        currentNode = currentNode.nextNode
    print(None)


def printNodeValueBackwards(tailNode):
    print("traversing backwards")
    print(tailNode.data, end=" => ")
    currentNode = tailNode.prevNode
    startNode = tailNode
    while (currentNode and currentNode != startNode):
        print(currentNode.data, end=" => ")
        currentNode = currentNode.prevNode

    print(None)

def printLowestValue(headNode:Node):
    print("determining lowest value")
    lowestValue = headNode.data
    currentNode = headNode.nextNode
    while (currentNode and currentNode != headNode):
        if(lowestValue > currentNode.data):
            lowestValue = currentNode.data
        currentNode = currentNode.nextNode
    print("lowest value is: ", lowestValue)

def deleteNodeFromList(node:'Node'):
    # store the links  to the previous and next nodes
    prevNodeInList:'Node' =  node.prevNode if node is not None else None
    nextNodeInList:'Node' = node.nextNode if node is not None else None

    # unlink the node to be deleted from the list
    if(prevNodeInList):
       prevNodeInList.nextNode = nextNodeInList
    
    if(nextNodeInList):
      nextNodeInList.prevNode = prevNodeInList

    # set the previous and next links of the node to be deleted to none
    node.prevNode = None
    node.nextNode = None

    print("dropped node ", node.data)

# call the functions
printNodeValueForwards(node1)
printNodeValueBackwards(node4)
printLowestValue(node1)

# delete node from list and traverse again
deleteNodeFromList(node1)
printNodeValueForwards(node1)
printNodeValueBackwards(node4)
printLowestValue(node2)

