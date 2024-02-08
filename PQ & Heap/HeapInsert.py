class Heap:
    def __init__(self):
        self._maxsize = 10
        self._data = [-1] * self._maxsize
        self._csize = 0

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def insert(self, e):
        if self._csize == self._maxsize:
            print('No Space in Heap')
            return
        self._csize = self._csize + 1
        hi = self._csize
        while hi > 1 and e > self._data[hi // 2]:
            self._data[hi] = self._data[hi // 2]
            hi = hi // 2
        self._data[hi] = e

    def max(self):
        if self._csize == 0:
            print('Heap is Empty')
            return
        return self._data[1]

S = Heap()
S.insert(25)
S.insert(14)
S.insert(2)
S.insert(20)
S.insert(10)
print(S._data)
S.insert(40)
print(S._data)


