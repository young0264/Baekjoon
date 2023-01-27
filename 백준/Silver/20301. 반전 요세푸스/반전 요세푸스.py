from collections import deque
n,k,m = map(int,input().split())

que = deque(range(1,n+1))
cnt = 0
while que: #0이면 오른쪽, 1이면 왼쪽
    if cnt//m % 2 == 0:
        for i in range(k-1):
            que.append(que.popleft())
    else:
        for i in range(k):
            que.appendleft(que.pop())
    cnt += 1
    print(que.popleft())


