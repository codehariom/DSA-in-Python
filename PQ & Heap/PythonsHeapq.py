import heapq as heap

L1 = []
heap.heappush(L1, 25)
heap.heappush(L1, 14)
heap.heappush(L1, 2)
heap.heappush(L1, 20)
heap.heappush(L1, 10)
heap.heappush(L1, 12)
heap.heappush(L1, 18)

print(L1)
e = heap.heappop(L1)
print('Removed Element:',e)
print(L1)
e = heap.heappop(L1)
print('Removed Element:',e)
print(L1)

heap.heappush(L1, 5)
print(L1)
e = heap.heappop(L1)
print('Removed Element:',e)
print(L1)

e = heap.heappushpop(L1, 35)
print('Removed Element:',e)
print(L1)

e = heap.heapreplace(L1, 8)
print('Removed Element:',e)
print(L1)

L2 = [20, 14, 2, 15, 10, 21]
print('Original List:',L2)
heap.heapify(L2)
print('List after Heapify:',L2)

L3 = heap.nsmallest(3, L2)
print('Smallest Elements:',L3)
L3 = heap.nlargest(3, L2)
print('Largest Elements:',L3)
