from collections import deque
r,c = map(int,input().split())
hx,hy = map(int,input().split())
ex,ey = map(int,input().split())
dxs,dys = [0,0,1,-1], [1,-1,0,0]
graph = [list(map(int,input().split())) for _ in range(r)]

visited = [[[0 for _ in range(2)] for _ in range(c)] for _ in range(r)]

def in_range(x,y):
    return 0<=x<r and 0<=y<c

def bfs(x,y):
    global answer
    que = deque()
    que.append((x,y,1))
    visited[x][y][1] = 1

    while que:
        dx,dy,cnt = que.popleft()

        if dx==ex-1 and dy==ey-1:
            answer = max(answer,visited[dx][dy][0],visited[dx][dy][1])
            return

        for i in range(4):
            nx,ny = dx+dxs[i] , dy+dys[i]
            if in_range(nx,ny) and not visited[nx][ny][cnt]:
                if graph[nx][ny] == 0:
                    visited[nx][ny][cnt] = visited[dx][dy][cnt] + 1
                    que.append((nx,ny,cnt))
                else:   #graph 가 1일때
                    if cnt > 0:
                        visited[nx][ny][cnt-1] = visited[dx][dy][cnt] + 1
                        que.append((nx, ny,cnt-1))
                    else:
                        continue
    return -1
answer = 0
bfs(hx-1,hy-1)
# print("asn",answer)
# for i in range(2):
#     answer=  max(answer,visited[ex-1][ey-1][i]-1)
print(answer-1)
