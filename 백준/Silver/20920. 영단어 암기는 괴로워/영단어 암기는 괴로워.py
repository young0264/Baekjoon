n,m = map(int,input().split())
dic = dict()
for i in range(n):
    s = input()
    if s not in dic:
        dic[s] = [1,len(s)]
    else:
        dic[s][0] += 1
# print(dic.items())
res = sorted(dic.items(), key=lambda x:(-x[1][0], -x[1][1],x[0]))

# res = (sorted(dic, key=lambda x :(x[1] ,x[0])))
for i in res:
    word = i[0]
    if len(word) < m:
        continue
    print(word)
