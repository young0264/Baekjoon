s = input()
answer = 0

arr = [97,101,105,111,117]
for i in s:
    if ord(i)  in arr:
        answer +=1
print(answer)
