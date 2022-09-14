import sys, heapq
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
heap = []
# arr = list(map(int,input().split()))
for i in range(n):
    arr = list(map(int,input().split()))
    if not heap:
        for j in arr:
            heapq.heappush(heap,j)
    else:
        for j in arr:
            if j > heap[0]:
                heapq.heappush(heap,j)
                heapq.heappop(heap)
print(heap[0])

