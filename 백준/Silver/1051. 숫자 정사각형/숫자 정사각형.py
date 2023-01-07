#N^3*4 50만
n,m = map(int,input().split())
graph = []
for _ in range(n):
    s = input()
    graph.append(list(map(int,s)))

min_num = min(n,m)
answer = 1
for k in range(min_num):
    for i in range(n-k):
        for j in range(m-k):
            if graph[i][j] == graph[i+k][j] == graph[i][j+k] == graph[i+k][j+k]:
                answer = max(answer,(k+1)*(k+1))
print(answer)