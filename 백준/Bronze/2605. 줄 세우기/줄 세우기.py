n = int(input())
arr = list(map(int,input().split()))
answer = [1]
for i in range(1,n):
    num = i+1
    line = i - arr[i]
    answer = answer[:line] + [num] + answer[line:]
print(*answer)