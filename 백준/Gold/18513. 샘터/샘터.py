from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
water = list(map(int, input().split()))

dic = dict()
answer = 0
que = deque()
for i in water:
    que.append(i)
    dic[i] = 1


def bfs():
    global answer, k
    while que:
        dx = que.popleft()

        for nx in [dx - 1, dx + 1]:
            if nx not in dic:
                dic[nx] = dic[dx] + 1
                k -= 1
                answer += dic[nx] - 1
                que.append(nx)
                if k == 0:
                    print(answer)
                    exit(0)


bfs()
