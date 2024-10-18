# creating stack in an explicit way 

class Stack:
    def __init__ (self):
        self.stack =[]
    
    def push(self,element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "stack empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0 
    
    def size(self):
        return len(self.stack)
    

myStack = Stack()

myStack.push("james")
myStack.push("loves")
myStack.push("to")
myStack.push("code")

print(myStack.stack)   # original  stack


myStack.pop()

myStack.push("dance")
print(myStack.stack)

a = myStack.peek()
print(a)
    
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()

b = myStack.isEmpty()
print(b)

myStack.push("james")
myStack.push("is")
myStack.push("back")
myStack.push("after")
myStack.push("the")
myStack.push("vacation")

c = myStack.size()
print(c)
