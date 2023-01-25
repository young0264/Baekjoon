import heapq


n = int(input())

heap = []
e_heap = []
answer = 1

for _ in range(n):
    num, start, end = map(int,input().split())
    heapq.heappush(heap, (start,end,num))

start,end,num, = heapq.heappop(heap)

e_heap.append(end)
while heap:
    s, e, number = heapq.heappop(heap)
    if s >= e_heap[0]:
        answer += 1
        # print(e_heap)
        # print(heap,answer)
        # print()
        heapq.heappop(e_heap)
    # else:
    heapq.heappush(e_heap,e)

print(len(e_heap))


