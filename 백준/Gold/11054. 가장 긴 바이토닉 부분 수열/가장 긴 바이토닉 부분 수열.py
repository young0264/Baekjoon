n = int(input())
arr = list(map(int, input().split()))

Ldp = [0] * n
Rdp = [0] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            Ldp[i] = max(Ldp[i], Ldp[j])
    Ldp[i] += 1

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[i] > arr[j]:
            Rdp[i] = max(Rdp[i], Rdp[j])
    Rdp[i] += 1


answer = 0
for i in range(n):
    answer = max(answer,Ldp[i]+Rdp[i]-1)
print(answer)