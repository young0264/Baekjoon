from collections import deque
def in_range(x):
    return 0<=x<100001

n,k = map(int,input().split())
move = [0]*100001
visited = [0]*100001

def bfs(subin, sister):
    que = deque()
    que.append(subin)
    visited[subin] = 1
    ans=[]
    while que:
        dx = que.popleft()
        if dx == sister:
            pos = dx
            for _ in range(visited[dx]):
                ans.append(pos)
                pos = move[pos]
            ans = (list(reversed(ans)))
            print(visited[sister]-1)
            print(*ans)
            return

        arr = [dx-1,dx+1,2*dx]
        for i in arr:
            if in_range(i) and not visited[i]:
                visited[i] = visited[dx]+1  #시간에 따른 방문처리를 해주고
                move[i]=dx
                que.append(i)

bfs(n,k)
