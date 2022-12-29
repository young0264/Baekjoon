import sys
input = sys.stdin.readline
n,m = map(int,input().split())
answer = 0
arr = []

for _ in range(n):
    s = input().rstrip()
    arr.append(s)

# for _ in range(m):
#     ns = input().rstrip()
#     for i in arr:
#         res = i.split(ns)
#         if len(res)==2 and res[0]=='':
#             answer+=1
#             break
for _ in range(m):
    ns = input().rstrip()
    length = len(ns)
    for i in arr:
        if i[:length] == ns:
            answer += 1
            break
print(answer)
# a = 'baekjoon'
# b = 'baekjoononlinejudge'

