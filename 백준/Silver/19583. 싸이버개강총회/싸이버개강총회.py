import sys
input = sys.stdin.readline
s,e,q = map(str,input().split())
dic = dict()
ns,ne,nq = 0,0,0

a,b =map(int, s.split(':'))
ns += a*60 + b
a,b =map(int, e.split(':'))
ne += a*60 + b
a,b =map(int, q.split(':'))
nq += a*60 + b
answer = 0
while True:
    k = input()
    if not k:
        break
    k = k.split(' ')
    a, b = k
    na,nb = map(int, a.split(':'))
    res = na*60 + nb # 시간

    if res <= ns:
        dic[b] = 1
    elif ne <= res <= nq and b in dic and dic[b] == 1:
        dic[b] -= 1
        answer += 1
print(answer)



