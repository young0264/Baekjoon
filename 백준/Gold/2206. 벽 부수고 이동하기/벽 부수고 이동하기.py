from collections import deque


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


graph = []
r, c = map(int, input().split())
for _ in range(r):
    graph.append(list(map(int,input())))
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
wall = 1
visited = [[[0]*2 for _ in range(c)] for _ in range(r)]

#[0,0] [0]은 파괴가능, [1]은 파괴 불가능
def bfs(x, y):
    visited[x][y][0] = 1
    que = deque()
    que.append((x, y,0))

    while que:
        dx, dy,dz = que.popleft()

        if dx == r - 1 and dy == c - 1:
            return visited[dx][dy][dz]

        for i in range(4):
            nx, ny = dx + dxs[i], dy + dys[i]
            if in_range(nx, ny) :
                if not graph[nx][ny] and not visited[nx][ny][dz]:
                    visited[nx][ny][dz] = visited[dx][dy][dz] + 1
                    que.append((nx, ny,dz))

                elif graph[nx][ny]==1 and dz==0:
                    visited[nx][ny][1] = visited[dx][dy][dz] + 1
                    que.append((nx, ny,1))



answer = bfs(0, 0)

if not answer:
    print(-1)
else:
    print(answer)
