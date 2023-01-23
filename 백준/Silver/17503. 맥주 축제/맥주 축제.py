import heapq

n, m, k = map(int, input().split())

arr = []
for _ in range(k):
    a,b = map(int,input().split())
    arr.append([a,b])
arr.sort(key = lambda x : x[1])

heap = []
sum_value = 0
answer = 0
for i in range(k):
    heapq.heappush(heap, arr[i][0])
    sum_value += arr[i][0]
    if len(heap) == n:
        if sum_value >= m:
            answer = arr[i][1]
            break
        else:
            sum_value-=heapq.heappop(heap)
    answer = -1
print(answer)


