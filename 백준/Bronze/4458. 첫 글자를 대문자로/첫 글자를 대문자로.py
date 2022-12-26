t = int(input())
for _ in range(t):
    s = list(input())
    if 97 <= ord(s[0])<=122:
        res = chr(ord(s[0])-32)
        s[0] = res
    print(''.join(s))