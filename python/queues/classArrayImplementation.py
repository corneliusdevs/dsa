class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data:any):
        self.queue.append(data)
    
    def dequeue(self):
        if(self.isEmpty()):
            return "queue is empty"
        return self.queue.pop(0)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def peek(self):
        return self.queue[-1]
    
    def clear(self):
        self.queue.clear()

    def size(self):
        return len(self.queue)
    
myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)

print("queue :", myQueue.queue)
print("dequeing :", myQueue.dequeue(), " size: ", myQueue.size(), " is empty: ", myQueue.isEmpty())
print("dequeing :", myQueue.dequeue(), " size: ", myQueue.size(), " is empty: ", myQueue.isEmpty())
print("dequeing :", myQueue.dequeue(), " size: ", myQueue.size(), " is empty: ", myQueue.isEmpty())
print("dequeing :", myQueue.dequeue(), " size: ", myQueue.size(), " is empty: ", myQueue.isEmpty())
print("dequeing :", myQueue.dequeue(), " size: ", myQueue.size(), " is empty: ", myQueue.isEmpty())

myQueue.enqueue(5)
myQueue.enqueue(6)


print("clearing :", myQueue.clear(), " size: ", myQueue.size(), " is empty: ", myQueue.isEmpty())
print("dequeing :", myQueue.dequeue(), " size: ", myQueue.size(), " is empty: ", myQueue.isEmpty())







