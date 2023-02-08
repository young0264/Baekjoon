a,b = map(str,input().split())

answer = 0


for i in a:
    for j in b:
        answer += int(i)*int(j)
print(answer)