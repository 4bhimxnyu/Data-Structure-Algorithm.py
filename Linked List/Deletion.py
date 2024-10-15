# Deletion in a linked list is done 

class Node:
    def __init__(self,data):
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
node4 = Node(56)
node5= Node(82)

node1.next=node2
node2.next=node3
node3.next = node4
node4.next = node5


print("Traversal before deletion of any node :" )
Traversal(node1)

def Deletion(head,nodetoDelete):
    if head == nodetoDelete:
        return head.next
    
    currentNode = head
    while currentNode.next != nodetoDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next

    return head


Deletion(node1,node3)

print("Traversal after deletion of the node")
Traversal(node1)

