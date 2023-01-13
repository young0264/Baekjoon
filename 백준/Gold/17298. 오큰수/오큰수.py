n = int(input())
arr = list(map(int,input().split()))
stack = [0]
answer = [-1]*n

for i in range(1,n):
    while stack:
        if arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            answer[idx] = arr[i]
        else:
            break
    stack.append(i)

print(*answer)