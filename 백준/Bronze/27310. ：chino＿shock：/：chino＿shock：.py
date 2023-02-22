s = input()
answer = len(s)
cnt = 0
for i in s:
    if i==':':
        answer += 1
    elif i=='_':
        cnt +=1
print(answer + cnt*5)