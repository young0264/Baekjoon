n = int(input())
arr = list(map(int,input().split()))
answer = 0
now = 0

for i in arr:
    if i == now:
        now += 1
        now = now%3
        answer+=1
print(answer)