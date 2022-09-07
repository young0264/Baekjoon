from collections import deque
r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]
answer = 0
dxs,dys = [-1,0,1,0],[0,1,0,-1],  #URDL
visited = [[0]*c for _ in range(r)]

def in_range(x,y):
    return 0<=x<r and 0<=y<c
def bfs(x,y):
    global answer,arr

    visited[x][y] = -1
    que = deque()
    que.append((x,y))
    arr.append([x,y])
    while que:
        dx,dy = que.popleft()
        # print("dx,dy",dx,dy)
        nx,ny = 0,0
        if graph[dx][dy] == 'U':
            nx,ny = dx + dxs[0], dy+dys[0]
        elif graph[dx][dy] =='R':
            nx,ny = dx + dxs[1], dy+dys[1]
        elif graph[dx][dy] =='D':
            nx,ny = dx + dxs[2], dy+dys[2]
        else:
            nx,ny = dx + dxs[3], dy+dys[3]

        #내부에서 탐색중일때
        if in_range(nx,ny) and visited[nx][ny]==0:
            visited[nx][ny] = visited[dx][dy] -1
            que.append((nx,ny))
            arr.append([nx,ny])
        elif in_range(nx,ny) and visited[nx][ny] < 0 :  #순환할때
            return False
        elif in_range(nx,ny) and visited[nx][ny] > 0:
            # print(" visited[dx][dy] = ", -visited[dx][dy])
            return -visited[dx][dy]
        elif not in_range(nx,ny):   #벗어나는 지점
            # print("-visited[dx][dy] = ",-visited[dx][dy])
            return -visited[dx][dy]

    return False



for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            arr = []
            res= bfs(i,j)
            if res:
                # print("i,j,res = ",i,j,res)
                answer += res
                for a,b in arr:
                    visited[a][b] = -visited[a][b]



print(answer)