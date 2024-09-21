# Create the node class
class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None

#  create instances of the nodes and assign them to a variable name
node1:Node = Node(3)
node2:Node = Node(4)
node3:Node = Node(5)
node4:Node = Node(6)
node5:Node = Node(7)
node6:Node = Node(8)


# link the lists together
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# print the values of the nodes
currentNode = node1

def deleteNode(headNode:Node, indexOfNodeToBeDeleted: int) -> Node | None:

    # this function returns the head node after deletng the node at the index specfied from the Linked List

    # traverse the list and stop at the index of the Node to be deleted  while getting the node at that Index

    previousNode:Node = None
    currentNode:Node = headNode
    nextNode:Node = currentNode.next
    currentIndex:int = 1

    while currentNode and currentIndex < indexOfNodeToBeDeleted:
        previousNode = currentNode
        currentNode = previousNode.next
        if(currentNode is not None):
          nextNode = currentNode.next
          currentIndex = currentIndex + 1

    
    if(currentNode is not None):
        #  unlink(delete) the currentNode from the List
        currentNode.next = None
    else:
        # if the program runs this block, it means the node at the indexOfNodeToBedeleted is none
        print("Node at index: ", indexOfNodeToBeDeleted, " does not exist!", "Index of the last node is: ", currentIndex)
        return headNode
        
    
    # set link the previousNode to the next node
    if(previousNode is not None):
       previousNode.next = nextNode

    # if we are deleting the headNode, then return the node after the head node as the new head Node
    if(indexOfNodeToBeDeleted == 1):
       return nextNode
    
    return headNode
    
        

  


def traverseList(headNode:Node):
    currentNode:Node = headNode
    while(currentNode):
        print(currentNode.data, end=" => ")
        currentNode = currentNode.next
    print(None, "\n")
    

def deleteNodeClean(headNode:Node, nodeToDelete:Node):
    if headNode == nodeToDelete:
        headNode.next = None
        return headNode.next
    
    currentNode = headNode
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return headNode
    
    currentNode.next = currentNode.next.next
    return headNode


def insertNodeInList(newNode:Node, headNode:Node, position:int) -> Node:
    if position == 1:
        newNode.next = headNode
        return newNode
    
    currentNode = headNode
    for _ in range(1, position - 1):
        if currentNode.next is None:
            break
        currentNode = currentNode.next
    
    newNode.next = currentNode.next
    currentNode.next = newNode

    return headNode


traverseList(node1)
traverseList(insertNodeInList(node6, node1, 100))
deleteNodeClean(node1, node3)
traverseList(node1)


            

       

            
         

        



