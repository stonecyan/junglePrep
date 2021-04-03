import heapq

li = [5, 7, 9, 1, 3]
heapq.heapify(li)

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)

# using heappop() to pop smallest element
heapq.heappop(li)


# using nlargest to print 3 largest numbers
print(heapq.nlargest(3, li))

# using nsmallest to print 3 smallest numbers
print(heapq.nsmallest(3, li))
