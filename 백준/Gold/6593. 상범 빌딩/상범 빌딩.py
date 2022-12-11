from collections import deque

def in_range(l,r,c):
    return 0<=l<L and 0<=r<R and 0<=c<C

def bfs():
    global start
    que = deque()
    x,y,z = start
    que.append(start)
    visited[z][x][y] = 1
    while que:
        dxs,dys,dzs = que.popleft()
        if dxs == ex and dys == ey and dzs == ez :
            return

        for i in range(6):
            nx,ny,nz = dxs+dx[i], dys+dy[i], dzs+dz[i]
            if in_range(nz,nx,ny) and not visited[nz][nx][ny] and graph[nz][nx][ny] != '#':
                visited[nz][nx][ny] = visited[dzs][dxs][dys] + 1
                que.append((nx,ny,nz))



while True:
    L, R, C = map(int,input().split())
    visited = [[[0]*C for _ in range(R)] for _ in range(L)]

    if L==0 and R==0 and C==0:
        break
    graph = []

    for i in range(L):
        ar = []
        for j in range(R):
            arr = list(input())
            ar.append(arr)
        x = input()
        graph.append(ar)
    start = -1,-1,-1 #행,렬,높이
    ex,ey,ez = -1,-1,-1
    dx,dy,dz = [0,0,-1,1,0,0],[1,-1,0,0,0,0],[0,0,0,0,1,-1] #동,서,남,북,상,하

    #====시작, 끝 위치 찾기====#
    for k in range(L):
        for i in range(R):
            for j in range(C):
                if graph[k][i][j] == 'S':
                    start = i,j,k
                elif graph[k][i][j] == 'E':
                    ex,ey,ez = i,j,k
    bfs()

    if visited[ez][ex][ey] == 0:
        print('Trapped!')
    else:
        print('Escaped in %d minute(s).' %(visited[ez][ex][ey]-1))







