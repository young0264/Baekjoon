from collections import defaultdict

# idx  0 1 2 3 4
# arr -1 0 0 1 1

def dfs(t):
    global leaf_node
    visited[t] = 1
    arr[t] = -2
    for i in range(n):
        if arr[i] == t:
            # visited[t] = 1
            dfs(i)

n = int(input())
visited = [0] * n
arr = list(map(int, input().split()))
m = int(input())
leaf_node = 0
# tree = defaultdict(list)

dfs(m)
# visited[m] = 1
# print(visited)
for i in range(n):
    if i not in arr and arr[i] != -2 :
        # print("i",i)
        leaf_node += 1
print(leaf_node)

#  0
#  1   4
# 5 2  5 6