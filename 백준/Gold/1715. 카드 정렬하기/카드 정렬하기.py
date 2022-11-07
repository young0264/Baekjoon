import heapq

n = int(input())
q = []
answer = 0


for i in range(n):
    card = int(input())
    heapq.heappush(q,card)

if n == 1:
    print(0)
    exit(0)
while q:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    answer += a+b
    if not q:
        break
    heapq.heappush(q,a+b)
print(answer)