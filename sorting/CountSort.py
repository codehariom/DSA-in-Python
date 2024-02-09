def countsort(A):
    n = len(A)
    maxsize = max(A)
    carray = [0] * (maxsize + 1)
    for i in range(n):
        carray[A[i]] = carray[A[i]] + 1
    i = 0
    j = 0
    while i < maxsize + 1:
        if carray[i] > 0:
            A[j] = i
            j = j + 1
            carray[i] = carray[i] - 1
        else:
            i = i + 1


A = [3, 5, 8, 9, 6, 2, 3, 5, 5]
print('Original Array:',A)
countsort(A)
print('Sorted Array:',A)






