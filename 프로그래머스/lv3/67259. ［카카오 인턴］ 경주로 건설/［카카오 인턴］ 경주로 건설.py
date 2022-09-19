import sys
def dfs(x,y,dir,res):
    global graph,answer
    value = 100
    if x==r-1 and y==c-1:
        # for i in visited:
            # print(*i)
        # print()
        # print("ans",answer)
        answer = min(answer,res)
        return
    for i in range(4):#동남서북
        nx,ny = x+dxs[i],y+dys[i]
        if in_range(nx,ny) and graph[nx][ny] != 1:

            if abs(dir-i) == 1 or abs(dir-i) == 3:
                value = 600
            else:
                value = 100
            if visited[nx][ny] :
                if visited[nx][ny] > visited[x][y] + value:
                    visited[nx][ny] = visited[x][y] + value
                    dfs(nx,ny,i,res+value)
            else:
                visited[nx][ny] = visited[x][y] + value
                dfs(nx,ny,i,res+value)
def in_range(x,y):
    global r,c
    return 0<=x<r and 0<=y<c

def solution(board):
    global r,c,dxs,dys,visited,graph,answer
    graph = board
    r,c = len(board) , len(board[0])
    dxs,dys = [0,1,0,-1],[1,0,-1,0]#동남서북
    answer = sys.maxsize
    visited = [[0]*c for _ in range(r)]
    visited[0][0] = 100
    dfs(0,0,1,0)
    visited = [[0]*c for _ in range(r)]
    dfs(0,0,2,0)

    # print(answer)
    return answer
