class Node:
    def __init__(self, data: any):
        self.data = data
        self.nextNode = None

class LinkedListStack:
    def __init__(self):
        self.headNode = None
        self.count = 0

    def push(self, data:any):
        # create a new node with the data.
        new_node = Node(data)
        # link the node
        if(self.headNode is None):
            self.headNode = new_node
            self.count = self.count + 1
            return
        # link the new_node to the self.head so that it becomes the headNode
        # store the new_node as the self.head
        new_node.nextNode = self.headNode
        self.headNode = new_node
        self.count = self.count + 1
    
    def pop(self):
        if(self.isEmpty()):
            return "stack is empty"
        popped_node = self.headNode
        # unlink the current self.headNode
        self.headNode = self.headNode.nextNode
        # update the count of the stack
        self.count = self.count - 1 
        return popped_node.data
    
    def isEmpty(self):
        return self.count == 0
    
    def peek(self):
        return self.headNode.data
    
    def clear(self):
        self.headNode = None
        self.count = 0
    
    def size(self):
        return self.count


myStack = LinkedListStack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)


print("last item ", myStack.peek(), " size: ", myStack.size())
print("popping ", myStack.pop(), " size :", myStack.size(), "peeking: ", myStack.peek())
print("popping ", myStack.pop(), " size :", myStack.size(), "peeking: ", myStack.peek())
print("last item ", myStack.peek(), " size: ", myStack.size())
print("is empty ", myStack.isEmpty(), " size: ", myStack.size())

myStack.push(5)
myStack.push(6)

print("last item ", myStack.peek(), " size: ", myStack.size())
print("popping ", myStack.pop(), " size :", myStack.size(), "peeking: ", myStack.peek())
print("is empty ", myStack.isEmpty(), " size: ", myStack.size())
print("clearing stack ", myStack.clear(), " size: ", myStack.size(), " is empty: ", myStack.isEmpty())












