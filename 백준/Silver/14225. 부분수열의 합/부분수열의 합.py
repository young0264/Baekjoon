n = int(input())
arr = list(map(int,input().split()))
arr.sort()
now = 0
answer = sum(arr)
for num in arr:
    if now+1 < num:
        answer = now
        break
    else:
        now += num
print(answer+1)
