
class Stack:
   def __init__(self):
      self.stack = []
   
   def push(self, item:any):
      self.stack.append(item)
      return self.stack
   
   def pop(self):
      if(self.isEmpty()):
         return "Stack is empty"
      return self.stack.pop()
      
   def isEmpty(self):
      return len(self.stack) == 0
   
   def peek(self):
      return self.stack[-1]
   
   def clear(self):
      self.stack.clear()
   
   def size(self):
      return len(self.stack)

# create a new Stack
myStack = Stack()

# push an item to the stack
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")

print(myStack.stack)

# pop items from the stack
print("popped an item: ", myStack.pop())
print("popped an item: ", myStack.pop())

# get the length of the stack 
print("stack lenth: ", myStack.size())

# clear items in the stack
print(myStack.clear())

# get the length of the stack 
print("stack lenth: ", myStack.size())