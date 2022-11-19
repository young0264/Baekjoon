na, nb = map(int,input().split())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))
#집합 a에는 속하면서 집합 b에는 속하지 않는  -> if a원소 in b

s = set(brr)
answer = []
for a in arr:
    if a not in s:
        answer.append(a)
if not answer:
    print(0)
else:
    print(len(answer))
    answer.sort()
    for i in answer:
        print(i,end=' ')
