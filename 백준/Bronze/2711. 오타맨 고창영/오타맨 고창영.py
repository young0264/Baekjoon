n = int(input())
for _ in range(n):
    m,s = map(str,input().split())
    m = int(m)
    res = s[:m-1] + s[m:]
    print(res)