from collections import deque
# x,y 격자 빼기로 하면. 지나갈 수 있는 경로에대해 오차가생김
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
sharkx, sharky, shark_size = 0, 0, 2
# graph[sharkx][sharky] = 0
for i in range(n):  # 상어위치찾기
    for j in range(n):
        if graph[i][j] == 9:
            sharkx,sharky = i, j

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

answer_dist = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x,y):
    global shark_size
    q = deque()
    q.append((x,y))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    arr = []

    while q:
        dx, dy = q.popleft()
        for i in range(4):
            nx,ny = dx+dxs[i], dy+dys[i]
            if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] <= shark_size:
                q.append((nx,ny))
                visited[nx][ny] = visited[dx][dy] + 1
                if 1 <= graph[nx][ny] < shark_size:
                # if graph[nx][ny]!=0 and graph[nx][ny] < shark_size:
                    arr.append((nx, ny, visited[nx][ny]-1))

    # if not arr:
    #     print(answer_dist)
    #     exit(0)
    res = sorted(arr, key=lambda x:(x[2],x[0],x[1]))
    return res

cnt = 0

while True:
    res = bfs(sharkx, sharky)
    if not res:
        print(answer_dist)
        break
    sx, sy, sd = res[0]
    graph[sx][sy] = 0 #
    graph[sharkx][sharky] = 0
    sharkx, sharky = sx,sy
    answer_dist += sd
    cnt += 1
    if shark_size == cnt:
        shark_size += 1
        cnt = 0

    # bfs(sharkx,sharky)






