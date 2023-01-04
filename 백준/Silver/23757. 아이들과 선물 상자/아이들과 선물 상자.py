import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
brr = list(map(int, input().split()))

arr = []
for i in a:
    heapq.heappush(arr, -i)


for i in brr:
    wish = i
    present = -heapq.heappop(arr)
    if present >= wish:
        heapq.heappush(arr,-(present-wish))
    elif present < wish:
        print(0)
        exit(0)


print(1)


