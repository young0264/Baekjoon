sss = list(map(str,input().split()))
arr = ''
ss = ''
for i in sss:
    ss+=i
for s in ss:
    arr += s[0]

answer = 'UCPC'
now = 0
res = ''

for s in ss:
    if s[0] == answer[now]:
        now += 1
        if now ==4:
            print('I love UCPC')
            exit(0)
print("I hate UCPC")