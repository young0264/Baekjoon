from collections import deque

n = int(input())
count = 0
arr = []

visited3 = [[] for _ in range(n+1)]
def bfs():
    que = deque()
    que.append(n)

    visited3[n] = [1,-1]    #-1이 나올 때 까지
    while que:
        dx = que.popleft()
        if dx==1:
            answer_arr = [1]
            rx = 1
            while True:
                if visited3[rx][1] == -1:
                    break
                else:
                    answer_arr.append(visited3[rx][1])
                    rx = visited3[rx][1]
            answer_arr.reverse()
            print(visited3[1][0]-1)
            print(*answer_arr)


            return
        for i in range(3):
            if i==0:
                if not dx%3:
                    nx = dx//3
                    if 0<nx<=n and not visited3[nx]:
                        visited3[nx] = [visited3[dx][0]+1, dx]
                        que.append(nx)

            elif i==1:
                if not dx%2:
                    nx = dx//2
                    if 0<nx<=n and not visited3[nx]:
                        visited3[nx] = [visited3[dx][0]+1, dx]
                        que.append(nx)
            else:
                nx = dx-1
                if 0 < nx <= n and not visited3[nx]:
                    visited3[nx] = [visited3[dx][0] + 1, dx]
                    que.append(nx)

bfs()

