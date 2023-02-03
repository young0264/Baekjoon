n = int(input())
dic = dict()
dic['ChongChong'] = 1

for _ in range(n):
    a, b = map(str,input().split())
    if a in dic and b not in dic:
        dic[b] = dic[a] + 1
    elif b in dic and a not in dic:
        dic[a] = dic[b] + 1

# print(max(dic.values()))
print(len(dic))