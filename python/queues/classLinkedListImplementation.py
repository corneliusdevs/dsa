
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class QueueLinkedList:
    def __init__(self):
        self.startNode = None
        self.lastNode = None
        self.count = 0 

    def enqueue(self, data:any):
        new_node = Node(data)
        if(self.isEmpty()):
            self.startNode = self.lastNode = new_node
            # update the count
            self.count = self.count + 1
            return
        self.lastNode.nextNode = new_node
        self.lastNode = new_node
        self.count = self.count + 1

    def dequeue(self):
        if(self.isEmpty()):
            return "Queue is empty"
        dequeued = self.startNode
        self.startNode = self.startNode.nextNode
        self.count = self.count - 1
        return dequeued.data
    
    def peek(self):
        if(self.isEmpty()):
            return "Queue is empty"
        return self.startNode.data
    
    def isEmpty(self):
        return self.count == 0
    
    def clearQueue(self):
        self.startNode = None
        self.lastNode = None
        self.count = 0
    
    def size(self):
        return self.count
    
    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        currentNode = self.startNode
        while(currentNode):
            print(currentNode.data, end=" => ")
            currentNode = currentNode.nextNode

print("  ")

myQueue = QueueLinkedList()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.enqueue(6)

print(myQueue.printQueue(), " count: ", myQueue.size())
print("dequeueing ", myQueue.dequeue(), " ", myQueue.printQueue(), " count: ", myQueue.size(), " peeking ", myQueue.peek())
print("dequeueing ", myQueue.dequeue(), " ", myQueue.printQueue(), " count: ", myQueue.size(), " peeking ", myQueue.peek())
print("dequeueing ", myQueue.dequeue(), " ", myQueue.printQueue(), " count: ", myQueue.size(), " peeking ", myQueue.peek())

myQueue.enqueue(7)
myQueue.enqueue(8)
print("dequeueing ", myQueue.dequeue(), " ", myQueue.printQueue(), " count: ", myQueue.size())
print("cleared que: ", myQueue.clearQueue(), " ", myQueue.printQueue(), " count: ", myQueue.size())





            

