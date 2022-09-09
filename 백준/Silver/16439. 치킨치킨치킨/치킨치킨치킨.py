from itertools import combinations
n,m = map(int,input().split())
number_arr = [i for i in range(m)]
answer = 0
graph = []

for i in range(n):
    arr = list(map(int,input().split()))
    graph.append(arr)

for combi in combinations(number_arr,3):
    # print("combi",combi)
    res = 0
    for i in range(n):
        a=0
        for j in combi:
            a=max(a,graph[i][j])
        res+=a
    answer = max(answer,res)
print(answer)
