#circular linked list is a data structure in which the head is connected to the tail of the list , which makes the data representation easier and circular

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

node1 = Node(3)
node2 = Node(33)
node3 = Node(333)
node4 = Node(3333)

node1.next = node2
node2.next = node3
node3.next = node4 
node4.next = node1

currentNode = node1
StartNode = node1

print("\n starting the node function\n")

print(currentNode.data , end = "-->")
currentNode = currentNode.next


while(currentNode != StartNode):
    print(currentNode.data , end = "-->")
    currentNode = currentNode.next

print("...")