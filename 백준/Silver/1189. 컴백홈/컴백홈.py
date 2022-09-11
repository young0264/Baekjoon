import sys
sys.setrecursionlimit(10**6)
r,c,k = map(int,input().split())
graph = []
dx,dy = [0,0,1,-1], [1,-1,0,0]
v = [[0]*c for _ in range(r)]
answer = 0
def in_range(x,y):
    return 0<=x<r and 0<=y<c
for i in range(r):
    graph.append(list(input()))

def dfs(x,y,visited):
    global answer

    if x==0 and y==c-1 and visited[x][y]==k:
        # print(x,y)
        answer +=1
        return

    for i in range(4):
        nx,ny = x+dx[i] , y+dy[i]
        if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny]!='T':
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx,ny,visited)
            visited[nx][ny] = 0

v[r-1][0] = 1
dfs(r-1,0,v)
print(answer)