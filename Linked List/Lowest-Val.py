# finding the lowest value in a linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def lowestVal(head):
    minValue = head.data
    currentNode= head.next
    while currentNode:
        if (currentNode.data < minValue ):
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

node1 = Node(389)
node2 = Node(78)
node3 = Node(34)
node4 = Node(898)

node1.next = node2
node2.next = node3
node3.next = node4

a = lowestVal(node1)


print("lowest value  in the linked list is: ", a )  

