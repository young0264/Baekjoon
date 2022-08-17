# 0,1 둘다 이동가능하지만 0일때 카운트를 해줘서  n,n도착햇을때 의 cnt중 최솟값 출력
import sys
from collections import deque
# dfs로 검은방 반문만 count해주고 min값 구하는거 아닌가
n = int(input())
graph = [list(map(int,input())) for _ in range(n)]  # 12줄
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n  # and not visited[x][y]

visited = [[0] * n for _ in range(n)]
def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = 1
    while que:
        dx,dy = que.popleft()
        for i in range(4):
            nx,ny = dx + dxs[i] , dy + dys[i],
            if in_range(nx,ny) and not visited[nx][ny]:
                if graph[nx][ny] == 0:#검은색벽
                    visited[nx][ny] = visited[dx][dy] + 1
                    que.append((nx,ny))
                else: #==1 : l흰색벽
                    visited[nx][ny] = visited[dx][dy]
                    que.appendleft((nx,ny))


bfs(0, 0)
answer = visited[n-1][n-1]
print(answer-1)
