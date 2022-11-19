import sys
input = sys.stdin.readline
r,c , b = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]
answer = [sys.maxsize,-sys.maxsize] #시간,높이

for h in range(0,257):
    cnt,time = 0,0
    for i in range(r):
        for j in range(c):
            res = h-graph[i][j]

            if res > 0:
                cnt += res
                time += res
            else:
                cnt += res
                time += abs(res)*2
    if cnt <= b:
        if answer[0] >= time:
            answer[0] = time
            answer[1] = h

for i in answer:
    print(i,end=' ')