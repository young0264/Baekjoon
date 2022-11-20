import heapq,sys
input = sys.stdin.readline
# xq = [1,1,1,3,5]
# print(heapq.heappop(xq))
# print(xq)
t = int(input())

#while 로직은 최소힙, 최대힙을 유지하기 위해 이미 연산된 값들을 지워주는 로직일 뿐

for i in range(t):
    min_q,max_q = [] , [] #각 index값의 2번째 값은 index j값
    n = int(input())
    visited = [0]*n
    for j in range(n):
        a, b = input().split()
        if a =='I':
            heapq.heappush(min_q,(int(b),j))
            heapq.heappush(max_q,(-int(b),j))
        else: # b=='D'
            if b=='-1':
                while min_q and visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = 1
                    heapq.heappop(min_q)
            else: #b=='1' 최대힙
                while max_q and visited[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = 1
                    heapq.heappop(max_q)

    while max_q and visited[max_q[0][1]]:
        heapq.heappop(max_q)
    while min_q and visited[min_q[0][1]]:
        heapq.heappop(min_q)
    if not min_q or not max_q:
        print("EMPTY")
    else:
        print("%d %d" %(-max_q[0][0], min_q[0][0]))





