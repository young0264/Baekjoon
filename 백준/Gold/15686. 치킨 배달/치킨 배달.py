from itertools import combinations
import sys

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = sys.maxsize
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])

for chicks in combinations(chicken, m):  # 골라진 치킨집 arr
    min_res = 0  # m개에서 최소거리값

    for hx, hy in home: #각 집에서 최소거리의 치킨집까지 갔을때의 값
        min_dist = sys.maxsize
        for cx, cy in chicks:
            min_dist = min(min_dist, (abs(hx-cx) + abs(hy-cy)))
        min_res += min_dist
    answer = min(answer,min_res)

print(answer)