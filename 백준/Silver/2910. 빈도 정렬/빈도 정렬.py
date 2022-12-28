n,c = map(int,input().split())
arr = list(map(int,input().split()))
dic = dict()

for i in arr:
    dic[i] = dic.get(i,0)+1

sorted_dic = sorted(dic.items(), key=lambda item:item[1],reverse=True )
# print(dic)

for i in sorted_dic:
    key =  i[0]
    for j in range(dic[key]):
        print(key,end=' ')