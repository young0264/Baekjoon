import sys, heapq

def dijkstra(s,e):
    global graph,length
    visited = [sys.maxsize]*(length+1)
    visited[s] = 0
    heap = []
    heapq.heappush(heap,[0,s])
    # heap.append([0,s])
    # heapq.heapify(heap)
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > visited[node]:
            continue

        for i in graph[node]: #graph : 노드, 코스트
            new_node, new_cost = i[0], i[1],
            new_cost += cost
            
            if new_cost < visited[new_node]:
                visited[new_node] = new_cost
                heapq.heappush(heap,[new_cost,new_node])
    return visited[e]

def solution(n, s, a, b, fares):
    global graph,length
    
    answer = sys.maxsize
    graph = [[] for _ in range(n+1)]
    length = n

    for i,j,cost in fares:
        graph[i].append([j,cost])
        graph[j].append([i,cost])
    for i in range(1,n+1):
        answer = min(answer,dijkstra(s,i)+ dijkstra(i,a)+dijkstra(i,b))
    return answer





    return answer