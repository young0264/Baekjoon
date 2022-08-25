a = (input())
b = (input())
flag = 0
res = ''

for i in a:
    if 65<=ord(i)<=91 or 97<= ord(i)<=122:
        res += i
if b in res:
    print(1)
else:
    print(0)

