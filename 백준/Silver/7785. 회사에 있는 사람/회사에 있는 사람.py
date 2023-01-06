n = int(input())
dic = dict()
arr = []
for _ in range(n):
    a,b, = map(str,input().split())
    if b == 'enter':
        dic[a] = 1
    else:
        dic[a] -= 1
for i in dic:
    if dic[i] == 1:
        arr.append(i)
arr.sort(reverse=True)
for i in arr:
    print(i)