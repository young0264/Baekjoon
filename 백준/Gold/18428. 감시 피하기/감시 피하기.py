from collections import deque

n = int(input())
graph = [list(map(str,input().split())) for _ in range(n)]
teacher_pos = []
dxs,dys=[0,0,1,-1],[1,-1,0,0]
answer = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teacher_pos.append((i,j))

def isTrueBfs():
    que = deque()
    for x,y in teacher_pos:
        que.append((x,y))
    while que:
        dx,dy = que.popleft() #선생님 하나 위치
        for dir in range(4):
            nx,ny = dx+dxs[dir], dy+dys[dir]
            while in_range(nx,ny):
                if graph[nx][ny] == 'S':
                    return False
                elif graph[nx][ny] == 'O':
                    break
                nx,ny = nx+dxs[dir],ny+dys[dir]

    return True

            # if in_range(nx,ny):
            #     if graph[nx][ny] == 'S':
            #         return False
            #     elif graph[nx][ny] == 'O':
            #         break
            #     que.append((nx,ny))
    # return True


def dfs(cnt):
    global answer

    if cnt == 3:
        if isTrueBfs():
            answer = 1
            return
    #cnt가 3인데 else일때
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    dfs(cnt+1)
                    graph[i][j] = 'X'

dfs(0)
if answer:
    print("YES")
else:
    print("NO")
