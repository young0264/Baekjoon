import heapq,sys
def input():
    return sys.stdin.readline().rstrip()

max_heap = [] #작은거 넣기
min_heap=[] #큰거 넣기
n = int(input())
arr = []
mid_value = 0
for i in range(n):
    # print(max_heap,min_heap)
    m = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap,(-m,m))
    else:
        heapq.heappush(min_heap,m)
    if min_heap and max_heap[0][1] > min_heap[0]:
        bigger = heapq.heappop(max_heap)[1]
        smaller = heapq.heappop(min_heap)
        heapq.heappush(min_heap,bigger)
        # heapq.heappush(max_heap,(smaller))
        heapq.heappush(max_heap,(-smaller,smaller))
    print(max_heap[0][1])