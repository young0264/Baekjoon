n = int(input())
graph = [list(map(str,input())) for _ in range(n)]
r,c = 0,0
for i in range(n):
    count, flag,connect = 0,0,0
    for j in range(n):
        if flag and not connect and graph[i][j]=='.':
            r += 1
            connect = 1

        if graph[i][j] =='.':
            flag = 1
        else:
            flag = 0
            connect = 0

for j in range(n):
    count, flag , connect = 0,0,0
    for i in range(n):
        if flag and not connect and graph[i][j] == '.':
            c += 1
            connect = 1

        if graph[i][j] == '.':
            flag = 1
        else:
            connect = 0
            flag = 0
print(r,c)