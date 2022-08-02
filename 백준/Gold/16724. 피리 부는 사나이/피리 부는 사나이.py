# 아 만약에 이전에 막아놓은 safe존의 그 통로로가면 자동으로 막히겟지 ㅂ임마!
r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]  ##동서남북 열행
num_dir = -1  # 동서남북
answer = 0

def in_range(x, y):  # 행열
    return 0 <= x < r and 0 <= y < c

def find_dir(x,y):
    if graph[x][y] == "R":
        return 0
    elif graph[x][y] == "L":
        return 1
    elif graph[x][y] == "D":
        return 2
    elif graph[x][y] == "U":
        return 3


def dfs(x, y, cnt):
    global answer
    visited[x][y] = cnt
    dir = find_dir(x,y)
    nx, ny = x + dx[dir], y + dy[dir]

    if in_range(nx,ny)  :
        if visited[nx][ny]==cnt:
            answer +=1
            return
        elif not visited[nx][ny]:
            dfs(nx,ny,cnt)


cnt = 0
for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            cnt += 1
            dfs(i, j, cnt)
print(answer)