
class Node:
    def __init__(self,data):
        self.Left = None
        self.Right = None
        self.data = data
    def printview(self):
        print(self.data)
Root = Node(10)
Root.printview()


