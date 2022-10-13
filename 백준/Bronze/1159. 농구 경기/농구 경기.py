n = int(input())
dic = dict()
for i in range(n):
    s = input()
    dic[s[0]] = dic.get(s[0],0)+1
# print(dic)
answer = []
for i in dic:
    if dic[i]>=5:
        answer.append(i)
answer.sort()
if not answer :
    print("PREDAJA")
else:
    print(''.join(answer))
