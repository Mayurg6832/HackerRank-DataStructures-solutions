class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        node=Node(val)
        #Enter you code here.
        if self.root==None:
            self.root=node
            return
        else:
            currentNode=self.root
            while True:
                if currentNode.info>val:
                    if currentNode.left == None:
                        currentNode.left=node
                        return
                    currentNode=currentNode.left
                else:
                    if currentNode.info<val:
                        if currentNode.right==None:
                            currentNode.right=node
                            return
                        currentNode=currentNode.right



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
