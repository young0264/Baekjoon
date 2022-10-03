n = int(input())
for i in range(n):
    s = input()
    res = ''
    for j in s:
        if 65 <= ord(j) <=90:
            res += chr(ord(j)+32)
        else:
            res += j
    print(res)