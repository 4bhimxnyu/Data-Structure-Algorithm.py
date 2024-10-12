# doubly linked list tells us the  node before and after the current node , that is the previous and the next data and address

class Node:
    def __init__ (self,data):
        self.data=data
        self.next = None
        self.prev= None

node1 = Node(3)
node2 = Node(33)
node3 = Node(333)
node4 = Node(3333)

node1.next = node2

node2.prev= node1
node2.next = node3

node3.prev= node2
node3.next = node4

node3.prev= node3

print("\n Traversal in forward direction")
currentNOde= node1

while currentNOde:
    print(currentNOde.data, end="-->")
    currentNOde=currentNOde.next

print("null")


print("\n Traversal in backward direction")
currentNOde = node4
while currentNOde:
    print(currentNOde.data, end="-->")
    currentNOde= currentNOde.prev

print("Head (First Value)")



