from collections import deque
#고슴도치 -> 비버 , 물과 고슴도치 상하좌우 이동
r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
dxs,dys = [0,0,1,-1],[1,-1,0,0]
bx,by = -1,-1
sx,sy = -1,-1   #고슴도치
wx,wy = -1,-1
answer = -1
que = deque()
def find_pos():
    global bx,by,sx,sy,wx,wy
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'D':
                bx,by = i,j
            elif graph[i][j] == 'S':
                sx,sy= i,j

def find_water():
    for i in range(r):
        for j in range(c):
            if graph[i][j] =='*':
                wx,wy = i,j
                que.append((i,j))
                visited[wx][wy] = -1
def in_range(x,y):
    return 0<=x<r and 0<=y<c

def bfs():
    global answer
    # que = deque()
    que.append((sx,sy))
    visited[sx][sy] = 1
    find_water()
    # 음수 -> 양수로 visited는 이동 가능.
    # 양수 -> 음수, 음수->음수 : 이동 불가능
    while que:
        dx,dy = que.popleft()
        # for i in visited:
        #     print(*i)
        # print()
        for i in range(4):
            nx,ny = dx+dxs[i], dy+dys[i]
            if in_range(nx,ny) and graph[nx][ny] != 'X':
                if graph[nx][ny] == 'D':
                    # print(dx,dy,nx,ny)
                    if visited[dx][dy] < 0:
                        continue
                    elif visited[dx][dy] > 0:
                        answer = visited[dx][dy]
                        return

                if not visited[nx][ny] :
                    if visited[dx][dy] > 0:
                        visited[nx][ny] = visited[dx][dy] + 1
                        que.append((nx,ny))
                    elif visited[dx][dy] < 0:
                        visited[nx][ny] = visited[dx][dy] - 1
                        que.append((nx,ny))

                elif visited[nx][ny] > 0:
                    if visited[dx][dy] < 0:
                        visited[nx][ny] = visited[dx][dy] - 1
                        que.append((nx,ny))







find_pos()
bfs()
# for i in visited:
#     print(*i)
if answer == -1:
    print('KAKTUS')
else:
    print(answer)
