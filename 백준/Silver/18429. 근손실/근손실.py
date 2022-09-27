n, k = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0
visited = [0]*n

def dfs(SBD,box):
    global answer
    if len(box) == n:
        # print(123123)
        # print(box)
        answer += 1
        return
    for i in range(n):
        if SBD-k+arr[i] < 500:
            continue
        elif not visited[i] :
            visited[i] = 1
            dfs(SBD-k+arr[i],box + [arr[i]])
            visited[i] = 0

# for i in range(n):
dfs(500,[])
print(answer)