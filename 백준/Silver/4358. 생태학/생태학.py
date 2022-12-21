import sys
input = sys.stdin.readline


dic = dict()
cnt = 0
arr = []
while True:
    s= input().rstrip()
    if not s:
        break
    dic[s] = dic.get(s,0)+1
    if dic[s] == 1:
        arr.append(s)
    cnt += 1

arr.sort()
for a in arr:
    res = dic[a]/cnt
    print(a,"{:.4f}".format(res*100))

    # print(a, round((res*100),4))