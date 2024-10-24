# first binary tree 

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
node1 = TreeNode('A')
node2 = TreeNode('B')
node3 = TreeNode('C')

node4 = TreeNode('D')
node5 = TreeNode('E')
node6 = TreeNode('F')
node7 = TreeNode('G')
node8 = TreeNode('H')
node9 = TreeNode('I')

root.left = node1 
root.right = node2

node1.left = node3
node1.right = node4

node2.left = node5
node2.right = node6

node3.left = node7
node3.right = node8

node5.right = node9

print("root.right.left.data: ", root.right.left.data )