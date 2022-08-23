import sys
def input():
    return sys.stdin.readline().rstrip()
n,q = map(int,input().split())
arr = [[] for _ in range(q+1)]
visited = [0]*(n+1)

# for i in range(1,n+1):
#     arr[i].append(i*2)
#     arr[i].append(i*2 +1)

for _ in range(q):
    t = int(input())
    target = t
    num = 0
    while target > 1:

        if visited[target] :
            num = target
        target = target//2

    #1까지 성공적으로 왔을때
    if not num:
        visited[t]=1
    print(num)