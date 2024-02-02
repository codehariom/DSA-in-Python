class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def insert(self,troot,e):
        temp = None
        while troot:
            temp = troot
            if e == troot._element:
                return
            elif e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right
        n = _Node(e)
        if self._root:
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n
        else:
            self._root = n

    def rsearch(self,troot,key):
        if troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                return self.rsearch(troot._left,key)
            elif key > troot._element:
                return self.rsearch(troot._right,key)
        else:
            return False

    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end=' ')
            self.inorder(troot._right)

B = BinarySearchTree()
B.insert(B._root,50)
B.insert(B._root,30)
B.insert(B._root,80)
B.insert(B._root,10)
B.insert(B._root,40)
B.insert(B._root,60)
B.insert(B._root,90)
B.inorder(B._root)
print()
print(B.rsearch(B._root,60))
print(B.rsearch(B._root,30))
print(B.rsearch(B._root,70))

