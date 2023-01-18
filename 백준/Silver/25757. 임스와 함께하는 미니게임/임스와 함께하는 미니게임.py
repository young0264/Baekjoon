n, s = map(str,input().split())
num = 0
if s=='Y':
    num = 2
elif s=='F':
    num = 3
else:
    num = 4
answer = 0
count = 1
dic = dict()

for i in range(int(n)):
    x = input()
    if x == '임스':
        continue
    else:
        if x not in dic:
            dic[x] = 1
            count += 1
            if count == num:
                answer += 1
                count = 1
print(answer)

