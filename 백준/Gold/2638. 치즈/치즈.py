from collections import deque
def in_range(x,y):
    return 0<=x<r and 0<=y<c
def check():
    flag = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] ==1 :
                flag = 1
            elif graph[i][j] == 2:
                graph[i][j] = 1
            elif graph[i][j] >=3:
                flag = 1
                graph[i][j] = 0
    if flag:
        return False
    else: return True


def bfs(x,y):
    visited = [[0]*c for _ in range(r)]
    visited[x][y] = 1
    que = deque()
    que.append((x,y))
    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny = dx+dxs[i], dy+dys[i]
            if in_range(nx,ny) and not visited[nx][ny]:
                if not graph[nx][ny]:
                    que.append((nx,ny))
                    visited[nx][ny] = 1
                else:   #graph[nx][ny] True
                    graph[nx][ny] += 1

dxs,dys = [0,0,1,-1],[1,-1,0,0]
r,c = map(int,input().split())
answer = 0
graph = [list(map(int,input().split())) for _ in range(r)]

while True:
    answer += 1
    bfs(0,0)
    if check():
        break
    else:
        continue
print(answer-1)



