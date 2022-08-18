from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

k = int(input())
c,r = map(int,input().split())
#k=1 이면 층은 2개가 있어야지
graph = [list(map(int,input().split())) for _ in range(r)]
dxs1, dys1 = [0,0,1,-1], [1,-1,0,0]
dxs2, dys2 = [-2,-2,-1,-1,1,1,2,2],[-1,1,-2,2,-2,2,-1,1]

def in_range(x,y):
    return 0<=x<r and 0<=y<c
#층을 만들고 열을만들고 행을만든다.
visited = [[[0]*(k+1) for _ in range(c)] for _ in range(r)]
def bfs(x,y,k):
    visited[x][y][k] = 1
    que = deque()
    que.append((x,y,k))
    while que:
        dx,dy,kk = que.popleft()
        if dx==r-1 and dy==c-1:
            return visited[dx][dy][kk]-1

        if kk >0:
            for i in range(8):
                nx,ny = dx+dxs2[i], dy+dys2[i],
                if in_range(nx,ny) and not visited[nx][ny][kk-1] and graph[nx][ny]==0:
                    visited[nx][ny][kk-1] = visited[dx][dy][kk] + 1 #다음이 kk-1
                    que.append((nx,ny,kk-1))


        for i in range(4):
            nx, ny = dx + dxs1[i], dy + dys1[i],
            if in_range(nx, ny) and not visited[nx][ny][kk] and graph[nx][ny] == 0:
                visited[nx][ny][kk] = visited[dx][dy][kk] + 1
                que.append((nx, ny, kk))
    return -1

answer= bfs(0,0,k)
print(answer)