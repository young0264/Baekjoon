from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

def in_range(x,y):
    return 0 <= x  and x+a-1 < n and 0 <= y  and y+b -1< m

def check(x,y):
    for i in range(x,x+a):
        for j in range(y,y+b):
            if graph[i][j] == 1:
                return False
    return True

dxs,dys = [0,0,1,-1],[1,-1,0,0]
n,m,a,b,k = map(int,input().split())
graph =[[0]*m for _ in range(n)]

for _ in range(k):
    bad1,bad2 = map(int,input().split())
    graph[bad1-1][bad2-1] = 1

#시작위치, 도착위치, index로 변환 -1
s1,s2 = map(int,input().split())
e1,e2 = map(int,input().split())
s1,s2,e1,e2 = s1-1,s2-1,e1-1,e2-1

if s1==e1 and s2==e2:
    print(0)
    exit(0)

visited=[[0]*m for _ in range(n)]
def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = 1

    while que:
        dx,dy = que.popleft()

        for i in range(4):
            nx,ny = dx+dxs[i], dy+dys[i]
            if in_range(nx,ny) and not visited[nx][ny] and check(nx,ny) :
                visited[nx][ny] = visited[dx][dy] + 1
                que.append((nx,ny))
                if nx==e1 and ny==e2:
                    return visited[dx][dy]

    return -1


for i in range(s1, s1 + a):
    for j in range(s2, s2 + b):
        if graph[i][j] == 1:
            print(-1)
            exit(0)

answer = bfs(s1,s2)
print(answer)
# for i in visited:
#     print(*i)
# print()
# for i in graph:
#     print(*i)
#




