answer = ''
graph = []
c = 0
for i in range(5):
    s = list(input())
    ls = len(s)
    res = s+(15-ls)*[-1]
    graph.append(res)

for j in range(15):
    for i in range(5):
        if graph[i][j] != -1:
            answer += graph[i][j]
print(answer)
