class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class DEQueLinked:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._front = newest
        else:
            self._rear._next = newest
        self._rear = newest
        self._size += 1

    def addfirst(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._front = newest
            self._rear = newest
        else:
            newest._next = self._front
            self._front = newest
        self._size += 1

    def removefirst(self):
        if self.isempty():
            print('DEQue is empty')
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isempty():
            self._rear = None
        return e

    def removelast(self):
        if self.isempty():
            print('DEQue is empty')
            return
        p = self._front
        i = 1
        while i < len(self) - 1:
            p = p._next
            i = i + 1
        self._rear = p
        p = p._next
        e = p._element
        self._rear._next = None
        self._size -= 1
        return e

    def first(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._front._element

    def last(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._rear._element

    def display(self):
        p = self._front
        while p:
            print(p._element,end=' --> ')
            p = p._next
        print()


D = DEQueLinked()
D.addfirst(5)
D.addfirst(3)
D.addlast(7)
D.addlast(12)
D.display()
print('Length:',len(D))
print(D.removefirst())
print(D.removelast())
D.display()
print(D.first())
print(D.last())
