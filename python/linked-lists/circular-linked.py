class CircularLinked:
    def __init__(self:'CircularLinked', data: int):
        self.data = data
        self.prevNode:'CircularLinked' = None
        self.nextNode: 'CircularLinked' = None

node1: 'CircularLinked' = CircularLinked(10)
node2: 'CircularLinked' = CircularLinked(2)
node3: 'CircularLinked' = CircularLinked(56)
node4: 'CircularLinked' = CircularLinked(-3)

node1.prevNode = node4
node1.nextNode = node2

node2.prevNode = node1
node2.nextNode = node3

node3.prevNode = node2
node3.nextNode = node4

node4.prevNode = node3
node4.nextNode = node1

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

def printLowestValue(headNode):
    print("determining lowest value")
    lowestValue = headNode.data
    currentNode = headNode.nextNode
    while currentNode != headNode:
        if(lowestValue > currentNode.data):
            lowestValue = currentNode.data
        currentNode = currentNode.nextNode
    print("lowest value is: ", lowestValue)

def deleteNodeFromList(node:'CircularLinked'):
    # store the links  to the previous and next nodes
    prevNodeInList = node.prevNode
    nextNodeInList = node.nextNode

    # unlink the node to be deleted from the list
    prevNodeInList.nextNode = nextNodeInList
    nextNodeInList.prevNode = prevNodeInList

    # set the previous and next links of the node to be deleted to none
    node.prevNode = None
    node.nextNode = None

    print("dropped node ", node.data)

# call the functions
printNodeValueForwards(node1)
printNodeValueBackwards(node4)

# delete node from list and traverse again
deleteNodeFromList(node4)
printNodeValueForwards(node1)
printNodeValueBackwards(node4)
printLowestValue(node1)


