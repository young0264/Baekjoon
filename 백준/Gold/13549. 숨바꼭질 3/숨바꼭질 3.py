from collections import deque
n,k = map(int,input().split())
#1,10만 ans=5, range 범위가 어케되나
def bfs(x):
    que=deque()
    visited = [0]*100001
    visited[x] = 1
    que.append(x)

    while que:
        dx = que.popleft()
        if dx==k:
            return visited[dx]
        nx_arr = [2*dx,dx+1, dx-1]

        for i in range(3):
            nx = nx_arr[i]
            if 0<= nx <=100000 and  not visited[nx]:
                if i == 0 :
                    visited[nx] = visited[dx]
                    que.appendleft(nx)
                elif i==1 or i==2:
                    visited[nx] = visited[dx]+1
                    que.append(nx)

print(bfs(n)-1)





