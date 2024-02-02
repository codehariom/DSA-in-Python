class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def rinsert(self,troot,e):
        if troot:
            if e < troot._element:
                troot._left = self.rinsert(troot._left,e)
            elif e > troot._element:
                troot._right = self.rinsert(troot._right,e)
        else:
            n = _Node(e)
            troot = n
        return troot

    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end=' ')
            self.inorder(troot._right)

B = BinarySearchTree()
B._root= B.rinsert(B._root,50)
B.rinsert(B._root,30)
B.rinsert(B._root,80)
B.rinsert(B._root,10)
B.rinsert(B._root,40)
B.rinsert(B._root,60)
B.rinsert(B._root,90)
B.inorder(B._root)

