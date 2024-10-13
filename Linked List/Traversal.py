# traversal in linked list is  O(n) where n is the number of nodes in the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def Traversal(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end="-->")
        currentNode = currentNode.next
    print("null")

node1= Node(5)
node2= Node(90)
node3 = Node(78)

node1.next=node2
node2.next=node3


Traversal(node1)
