import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
dic1 = dict()
dic2 = dict()
service_dic = dict()
price = 0

for _ in range(a):
    menu, p = map(str,input().split())
    dic1[menu] = int(p)

for _ in range(b):
    menu, p = map(str,input().split())
    dic2[menu] = int(p)

for _ in range(c):
    menu = input()
    service_dic[menu] = service_dic.get(menu,0)+1

n = int(input())
price = 0
arr = []
brr = []
for _ in range(n):
    menu = input().rstrip()
    if menu in dic1:
        price += dic1[menu]
    else:
        if menu in dic2:
            arr.append(menu)
        else:
            brr.append(menu)
if price >= 20000:
    for a in arr:
        price += dic2[a]
else:
    if arr:
        print("No")
        exit(0)
# print(price)

if price >= 50000:
    if len(brr) > 1:
        print("No")
        exit(0)
else:
    if brr :
        print("No")
        exit(0)

print("Okay")





