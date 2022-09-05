from itertools import combinations
import sys
n = int(input())
taste_arr = []
answer = sys.maxsize

for i in range(n):
    s, ss = map(int,input().split())
    taste_arr.append((s,ss))

for i in range(1,n+1):
    for combi in combinations(taste_arr,i):
        res1,res2 = 1,0
        for a,b in combi:
            res1 *= a
            res2 += b
        answer = min(answer,abs(res1-res2))
print(answer)