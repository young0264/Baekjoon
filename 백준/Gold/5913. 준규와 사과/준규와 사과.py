n = int(input())
graph = [[0]*5 for _ in range(5)]
dxs,dys = [0,0,1,-1],[1,-1,0,0]
visited = [[0]*5 for _ in range(5)]
answer = 0

for i in range(n):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 2 #2는 사과가 없어, 이동하면 안되는곳

def in_range(x,y):
    return 0<=x<5 and 0<=y<5

def isTrueDist():
    for i in range(5):
        for j in range(5):
            if graph[i][j] == 0 and not visited[i][j]:
                return False
    return True

def dfs(x,y):
    global answer
    # print(x,y)
    for i in range(4):
        nx,ny = x+dxs[i], y+dys[i]
        if nx==4 and ny==4:
            visited[nx][ny] = 1
            if isTrueDist():
                answer += 1
        if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny]==0:
            visited[nx][ny] = 1
            dfs(nx,ny)
            visited[nx][ny] = 0
visited[0][0] = 1
dfs(0,0)
print(answer)