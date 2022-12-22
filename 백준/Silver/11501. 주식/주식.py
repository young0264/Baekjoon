t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    now = arr[-1]
    for i in range(-2,-n-1,-1):
        if arr[i] > now:
            now = arr[i]
        else:
            cnt += now - arr[i]
        # print(now)
    print(cnt)