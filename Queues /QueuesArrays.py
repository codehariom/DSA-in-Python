class QueuesArray:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.isempty():
            print('Queue is empty')
            return
        return self._data.pop(0)

    def first(self):
        if self.isempty():
            print('Queue is empty')
            return
        return self._data[0]


Q = QueuesArray()
Q.enqueue(5)
Q.enqueue(3)
print('Queue:',Q._data)
print('Queue Length:', len(Q))
ele = Q.dequeue()
print('Queue:',Q._data)
print('Queue Length:', len(Q))
print('Removed Element:',ele)
print('Is Queue Empty:',Q.isempty())
Q.enqueue(7)
print('Queue:',Q._data)
print('Queue Length:', len(Q))
Q.enqueue(12)
print('Queue:',Q._data)
print('Queue Length:', len(Q))
ele = Q.dequeue()
print('Queue:',Q._data)
print('Queue Length:', len(Q))
print('Removed Element:',ele)
print('First Element:',Q.first())
