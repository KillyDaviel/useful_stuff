class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    q=[root]
    d=dict()
    root.level=0
    while len(q)!=0:
        root=q.pop(0)
        if root.level not in d:
            d[root.level]=root.info
        if root.left is not None:
            q.append(root.left)
            root.left.level=root.level-1
        if root.right is not None:
            q.append(root.right)
            root.right.level =root.level+1
    lst=[i for i in sorted(d.keys())]
    for i in lst:
        print(d[i],end=" ")  



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)