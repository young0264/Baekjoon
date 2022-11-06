import heapq
n,m = map(int,input().split())
arr = list(map(int,input().split()))
q = []
for i in arr:
    heapq.heappush(q,i)
for i in range(m):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    res = a+b
    heapq.heappush(q,res)
    heapq.heappush(q,res)
print(sum(q))
