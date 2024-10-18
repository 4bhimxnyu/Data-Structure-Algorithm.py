# creating the queue in more traditional and explicit way

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "queue empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "queue empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue)== 0 
    
    def size(self):
        return len(self.queue)
    

myQueue = Queue()

myQueue.enqueue("james")
myQueue.enqueue("loves")
myQueue.enqueue("to")
myQueue.enqueue("code")

print(myQueue.queue)

myQueue.dequeue()
print(myQueue.queue)

a = myQueue.peek()
print(a)

b = myQueue.isEmpty()
print(b)

c = myQueue.size()
print(c)
