from collections import deque

n, m = map(int, input().split())
visited = [0] * (n + 1)
que = deque()
parking = []
weight = []
answer = 0
dic = dict()
for _ in range(n):
    k = int(input())
    parking.append(k)

for _ in range(m):
    k = int(input())
    weight.append(k)

for _ in range(m * 2):
    k = int(input())
    if k > 0:
        flag = 0
        for i in range(n):  # i : 주차공간 자리
            if not visited[i] :
                visited[i] = k  # idx
                flag= 1
                break
        if not flag:
            que.append(k)

    else:
        idx = 0
        for i in range(n):
            if visited[i] == -k:
                visited[i] = 0
                idx = i
                break
        answer += (weight[-k-1])*parking[idx]
        # print("idx : " , idx)
        if que:
            visited[idx] = que.popleft()  # q = k번째 차량무게 인덱스

        # print(weight[-k-1],parking[idx])

print(answer)

# 주차 공간들의 단위 무게당 요금
# 번호가 가장 작은 주차공간에 주차
