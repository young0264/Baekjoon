import heapq
t = int(input())
q = []
for i in range(t):
    arr = list(map(int,input().split()))
    if arr[0] != 0:
        for j in range(arr[0]):
            heapq.heappush(q,-arr[j+1])
    else:
        if q:
            print(-heapq.heappop(q))

        else:
            print(-1)
