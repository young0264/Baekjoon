n = int(input())
dic = dict()
for _ in range(n):
    fruit, num = map(str,input().split())
    dic[fruit] = dic.get(fruit, 0) + int(num)

for key in dic:
    if dic[key] == 5:
        print("YES")
        exit(0)
print("NO")




