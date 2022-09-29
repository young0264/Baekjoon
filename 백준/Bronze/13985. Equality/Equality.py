s = input().split('=')
res = s[0].split('+')

if int(res[0])+int(res[1])==int(s[1]):
    print("YES")
else:
    print("NO")