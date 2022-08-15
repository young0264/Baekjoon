from collections import deque
def solution(places):
    answer = []
    
    dxs,dys = [0,0,1,-1],[1,-1,0,0]
    
    def in_range(x,y):
        return 0<=x<5 and 0<=y<5
    
    def bfs(x,y):
        que = deque()
        que.append((x,y))
        visited = [[0]*5 for _ in range(5)] 
        visited[x][y] = 1

        while que:
            dx,dy = que.popleft()
            
            for i in range(4):
                nx,ny = dx+dxs[i] , dy+dys[i]
                if in_range(nx,ny) and not visited[nx][ny]:
                    visited[nx][ny] = 1

                    if place[nx][ny] == 'P':
                        if abs(x-nx) + abs(y-ny) <= 2:
                            return False
                    elif place[nx][ny] =='O' and (abs(x-nx) + abs(y-ny))==1:
                        visited[nx][ny] = 1
                        que.append((nx,ny))
        return True
    
    for place in places:
        P_arr = []
        flag = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    #P_arr.append((i,j))
                    res= bfs(i,j)
                    if not res:
                        flag = 1
                
        if not flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer