# insertion in a linked list is done  by creating a new node and linking it to the previous node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def Traversal(head):
    currentNode = head
    while(currentNode):
        print(currentNode.data, end = "-->")
        currentNode = currentNode.next
    print("Null")

node1 = Node(56)
node2 = Node(42)
node3 = Node(67)
node4 = Node(78)
node5 = Node(21)

node1.next= node2
node2.next = node3
node3.next = node4
node4.next = node5

Traversal(node1)