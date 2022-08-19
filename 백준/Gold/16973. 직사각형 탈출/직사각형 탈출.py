from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()
r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

# 직사각형가로세로, 시작점, 도착점
h, w, sx, sy, fx, fy = map(int, input().split())
h, w, sx, sy, fx, fy = h - 1, w - 1, sx - 1, sy - 1, fx - 1, fy - 1
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
arr = []

for i in range(r):
    for j in range(c):
        if graph[i][j] == 1:
            arr.append([i,j])

def check(x,y):
    for a,b in arr:
        if x <= a < x+h+1 and y <= b <y+w+1:
            return False
    return True

def in_range(x, y):  # x+h-1 , y+h-1 //
    return 0 <= x and 0 <= y and x + h < r and y + w < c


visited = [[0] * c for _ in range(r)]


def bfs(x, y):
    visited[x][y] = 1

    que = deque()
    que.append((x, y))

    while que:
        dx, dy = que.popleft()

        if dx == fx and dy == fy:
            return visited[dx][dy] - 1

        for i in range(4):
            nx, ny = dx + dxs[i], dy + dys[i]
            if in_range(nx, ny) and check(nx, ny) and not visited[nx][ny] and not graph[nx][ny]:
                visited[nx][ny] = visited[dx][dy] + 1

                que.append((nx, ny))
    return -1


answer = bfs(sx, sy)

print(answer)
