from Heaps import Heap

def heapsort(A):
    H = Heap()
    n = len(A)
    for i in range(n):
        H.insert(A[i])
    k = n-1
    for i in range(H._csize):
        A[k] = H.deletemax()
        k = k - 1


A = [63, 250, 835, 947, 651, 28]
print('Original Array:',A)
heapsort(A)
print('Sorted Array:',A)


