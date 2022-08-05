arr = list(map(int,input().split()))
brr = [1,1,2,2,2,8]
answer = []
for i in range(6):
    res = brr[i]-arr[i]
    answer.append(res)
print(*answer)