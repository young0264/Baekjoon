import sys
input = sys.stdin.readline

k, l = map(int,input().split())
dic = {}
arr = []
for i in range(l):
    s = input()
    arr.append(s)
    dic[s] =  dic.get(s,0)+1
# print(dic)
for s in arr:
    if dic[s] == 1:
        k-=1
        print(s.rstrip())
        if k==0:
            break
    else:
        dic[s] -= 1
