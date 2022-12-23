a,b = map(int,input().split())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))
dic_A = {}
dic_B = {}
answer = 0
for i in arr:
    dic_A[i] = 1
for i in brr:
    dic_B[i] = 1
for i in dic_A:
    if i not in dic_B:
        answer += 1

for i in dic_B:
    if i not in dic_A:
        answer += 1
print(answer)