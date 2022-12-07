from itertools import product
import sys
input = sys.stdin.readline
n = int(input())

arr = list(map(str,[0,1,2]))
answer = 0

for permu in product(arr,repeat=n):
    res = ''
    for i in permu:
        res+=i
    if int(res)%3==0 and len(str(int(res)))==n:
        # print(res)
        answer += 1
if n==1:
    print(0)
else:
    print(answer)