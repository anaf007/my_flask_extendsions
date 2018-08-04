#coding=utf-8
"""
二叉树
"""
class BTree():

    def __init__(self,value):
        self.lef = None
        self.data = value
        self.right = None

    def insertLeft(self,value):
        self.left = BTree(value)
        return self.left

    def insertRight(self,value):
        self.right = BTree(value)
        return self.right

    def show(self):
        print(self.data)

if __name__ == '__main__':
    Root = BTree('Root')
    A = Root.insertLeft('A')
    B = Root.insertRight('B')

    C = A.insertLeft('C')
    D = A.insertRight('D')
    F = D.insertLeft('F')
    G = D.insertRight('D')
    
    E = B.insertLeft('E')
    Root.show()
    Root.left.show()
    Root.right.show()
    A = Root.left
    A.show()

        