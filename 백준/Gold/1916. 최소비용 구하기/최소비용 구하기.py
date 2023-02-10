import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = sys.maxsize
graph = [[] for _ in range(n+1)]
#a에서 b까지의 거리인 c [a]=(b,c)
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))


start, end = map(int,input().split())

visited = [0]*(n+1)
distance = [INF]*(n+1)
def djk():
    dist, node = 0,start
    q = []
    heapq.heappush(q, (dist,node))
    while q:
        d, now = heapq.heappop(q) #거리와, 현재노드
        if distance[now] < d:
            continue
        # if not visited[now]:
        for i in graph[now]:
            cost = d+i[1]
            # distance[i[1]] = min(distance[i[1]], cost)
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
        # visited[now] = 1
    # print(distance)
djk()
print(distance[end])