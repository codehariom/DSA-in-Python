def bubblesort(A):
    n = len(A)
    for passes in range(n-1,0,-1):
        for i in range(passes):
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp


A = [3, 5, 8, 9, 6, 2]
print('Original Array:',A)
bubblesort(A)
print('Sorted Array:',A)
