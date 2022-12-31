import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dic = dict()

for _ in range(n):
    s = input().rstrip()
    dic[s] = 1
# print(dic)
for _ in range(m):
    arr = input().rstrip().split(',')
    for i in arr:
        if i in dic and dic[i] == 1:
            dic[i] -= 1
            n -= 1
    print(n)

# 뭐가 포인트지,