class Node:
    def _init_(self,data):
        self.data =data
        self.next = None


harry = Node(3)
bruce = Node(5)
john = Node(22)
mario = Node(18)

harry.next =  bruce
bruce.next = john
john.next = mario

currentNode = harry

while currentNode:
    print(currentNode.data , end = "-->")
    currentNode = currentNode.next

print("null")