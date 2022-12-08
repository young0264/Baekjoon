#방향성 있는 다익스트라
import heapq, sys
input = sys.stdin.readline
V,E = map(int,input().split())
INF = sys.maxsize
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)
for i in range(E):
    u,v,w = map(int,input().split())
    # graph[u][v] = w
    graph[u].append((v,w))#도착v , 거리w

def dijk(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        else:
            for a,b in graph[now]:
                res = distance[now] + b
                if res < distance[a]:
                    distance[a] = res
                    heapq.heappush(q,(res,a))

dijk(start)
for i in range(1,V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

