import heapq

# arr = [16,2,3,5,7]
# q = []
# for i in arr:
#     heapq.heappush(q,-i)
# print("h1", heapq.heappop(q))
# print("heapq ", q)

#
n = int(input())
dasom = -1
arr = []
cnt = 0
for i in range(n):
    if i == 0:
        dasom = int(input())
    else:
        heapq.heappush(arr, -int(input()))

if n == 1:
    print(0)
    exit(0)
while dasom <= -arr[0]:
    q = heapq.heappop(arr) #음수
    dasom += 1
    heapq.heappush(arr, (q + 1))
    cnt += 1
# print("arr",arr)
print(cnt)
