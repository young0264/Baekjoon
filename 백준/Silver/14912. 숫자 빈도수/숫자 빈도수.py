n,d = map(int,input().split())
answer = 0
for i in range(1,n+1):
    for j in str(i):
        if int(j) == d:
            answer += 1
print(answer)