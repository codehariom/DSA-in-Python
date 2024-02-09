def binarysearch_iterative(A, key):
    l = 0
    r = len(A)-1
    while l <= r:
        mid = (l + r) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            r = mid - 1
        elif key > A[mid]:
            l = mid + 1
    return -1

A = [15,21,47,84,96]
found = binarysearch_iterative(A,84)
print('Result: ',found)
