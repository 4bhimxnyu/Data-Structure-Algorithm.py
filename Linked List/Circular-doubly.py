# Circular doubly linked List is a data structure  in which the next pointer of the last node points to the first node and the previous pointer of the
# first node points to the last node.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(3)
node2 = Node(33)
node3 = Node(333)
node4 = Node(3333)

node1.prev = node4
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node1

print("\n Traversal in forward Direction")

currentNode = node1 
StartNode = node1

print(currentNode.data,end = "-->")
currentNode = currentNode.next

while currentNode !=  StartNode:
    print(currentNode.data , end = "-->")
    currentNode = currentNode.next
print("...")


print("\n Traversal in Backward Direction")

currentNode = node4
StartNode = node4

print(currentNode.data, end= "-->")
currentNode = currentNode.prev

while (currentNode != StartNode):
    print(currentNode.data, end = "-->")
    currentNode = currentNode.prev

print("...")

