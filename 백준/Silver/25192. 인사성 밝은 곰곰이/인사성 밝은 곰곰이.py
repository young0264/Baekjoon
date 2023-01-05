n = int(input())
s = set()
flag = 0
cnt = 0
for _ in range(n):
    k = input()
    if k == 'ENTER':
        flag = 1
        cnt += len(s)
        s = set()
    else:
        s.add(k)
cnt += len(s)
print(cnt)
