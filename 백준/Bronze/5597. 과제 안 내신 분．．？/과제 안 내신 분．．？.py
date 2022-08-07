arr = [0]*30
answer = []
for i in range(28):
    n = int(input())
    arr[n-1] = 1
for i in range(30):
    if arr[i] ==0:
        answer.append(i+1)
print(answer[0])
print(answer[1])
