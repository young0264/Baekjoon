n = int(input())
dic = dict()
for _ in range(n):
    s = input()
    dic[s] = dic.get(s,0)+1
for _ in range(n-1):
    s = input()
    dic[s] -= 1
for i in dic:
    if dic[i] == 1:
        print(i)
        break